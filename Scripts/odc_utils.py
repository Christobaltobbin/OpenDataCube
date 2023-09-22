# import and necessary libraries
import dask.distributed
import dask.utils
import numpy as np
import planetary_computer as pc
import xarray as xr
from IPython.display import display
from pystac_client import Client
import matplotlib.pyplot as plt
import folium

from odc.stac import configure_rio, stac_load

# Function to configure the data loading priocess
def configure_asset():
    configuration = {
            "sentinel-2-l2a": { # we specify the name of the data collection
                "assets": { # call the asset dictionary under the data collection and load the sub-dictionaries
                    "*": {"data_type": "uint16", "nodata": 0},
                    "SCL": {"data_type": "uint8", "nodata": 0},
                    "visual": {"data_type": "uint8", "nodata": 0},
                },
            },
            "*": {"warnings": "ignore"},# applies this to all assets within the data collection
        }
    return configuration

# Function to manage and coordinate distributed computation using dask
def client_info():
    client = dask.distributed.Client() # create a dask disrtributed client which allows to manage and coordinate distributed computations.
    configure_rio(cloud_defaults=True, client=client)
    display(client) #display client
    return client

# Function to pull image data collection
def get_data_collection(client, collection, date, tile_id):
    data_catalog = client # client data source

    query = data_catalog.search(
        collections= [collection],# call the data collection, this time we want to call the sentinel 2 data collection 
        datetime= date, # cloudfree date 
        query={"s2:mgrs_tile": dict(eq= tile_id)}, # we select a specific tile from northern parts of Ghana, 'Janga'
    )
    
    # list the number of dataset, but this time we only need one
    images = list(query.items()) 
    
    # print the number of datasets found
    print(f"Found;{len(images):d} datasets") 
    # we expect a single dataset since we selected a single day
    return images

# Function to Lazy load entire bands in data collection
def load_dataset_with_resolution(images, configuration, resolution):
    # specify the parameters
    dataset = stac_load(
        images, chunks={"x":2048, "y":2048},
        stac_cfg=configuration, patch_url=pc.sign,
        resolution=resolution,
    )
    
    # list the bands in the dataset
    print(f"Bands: {','.join(list(dataset.data_vars))}")
    
    #display the dataset
    display(dataset)
    
    return dataset

# Function to select specific bands
def select_bands(images, configuration, resolution):
    dataset = stac_load(
        images, bands=["red", "green", "blue", "nir", "SCL"],# select needed bands
        chunks={"x":2048, "y":2048},
        stac_cfg=configuration, patch_url=pc.sign,
        resolution=resolution,
    )
    
    # List the selected bands
    print(f"Bands: {','.join(list(dataset.data_vars))}")
    
    # Display the dataset
    display(dataset)
    
    return dataset

# Function to convert data to float
def to_float(dataset):
    dataset_float_1 = dataset.astype("float32")
    nodata_1= dataset_float_1.attrs.pop("nodata", None)
    if nodata_1 is None:
        return dataset_float_1
    return dataset_float_1.where(dataset != nodata_1)
