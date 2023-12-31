# OpenDataCube For NDVI and LAI 

## Introduction
The Open Data Cube (ODC) is an open-source geospatial data management and analysis platform designed for working with large, multi-dimensional Earth observation (EO) and remote sensing data. NDVI and LAI are very important vegetation indices which contribute greatly in the monitoring of vegetation health and density. In this project, we assessed the ODC from Microsoft Planetory Computer. This project aims to assess ODC data collection over a region in Ghana, Janga and compute for the NDVI and LAI for 2020 and 2023 respectively. 

## Study Area
Janga is a town located in the northeastern part of Ghana, specifically in the North East Region. It is situated at latitude 10°01'52"N and longitude 00°58'37"W. I chose the 30PYS sentinel two tile since Janga falls within it.

## Method
I wrote a python script which assesses Sentinel 2A data from Microsoft Planetory Computer ODC. Loaded the bands and performed math on them to compute the NDVI and LAI values of the studio region for 2023 and 2020 respectively. Then went ahead and computed the mean and standard deviations for the NDVI and LAI values and generated a histogram plot to compare the results. You can see the full script in the Scripts folder in this repository.

## Results
After computing for the NDVI and the LAI for the year 2023 I had the following NDVI(left) and LAI(right) values:

<p align="center">
  <img src="https://github.com/Christobaltobbin/Drought_Assessment/assets/116877317/69ad5fef-536f-4bb4-805d-5262f01efbe4.png" align="left" width="385" height="350">
  <img src="https://github.com/Christobaltobbin/Drought_Assessment/assets/116877317/ab9739b7-5274-41da-82e3-eb21af8cca2f.png" align="right" width="385" height="350">
</p>


After computing for the NDVI and the LAI for the year 2020 I had the following NDVI(left) and LAI(right) values:


<p align="center">
  <img src="https://github.com/Christobaltobbin/Drought_Assessment/assets/116877317/37164d1a-31a7-4394-93c5-81d26bebc178.png" align="left" width="385" height="350">
  <img src="https://github.com/Christobaltobbin/Drought_Assessment/assets/116877317/6fa60225-233f-45c3-80ab-fe18a1411fcd.png" align="right" width="385" height="350">
</p>


The mean NDVi value for 2023 was 0.128 while that for 2020 was 0.251. This goes to say that the vegetation density in Janga for the year 2020 was greater than that of 2023. The NDVI standard deviation(SD) values for 2023 was 0.042 and 0.085 for 2020. The SDs indicate a higher vegetation variability in Janga for the year 2020 as compared to 2023. The mean LAI value for 2023 was 0.773 and for 2020 was 1.047, also the standard deviation values were 0.084 and 0.247 respectively. These results follow the pattern of the NDVI values indicating that there has been a reduction in vegeation in Janga from 2020 to 2023.


The histograms also indicate that the vegetation in Janga has depreciated from 2020 to 2023, below are the histogram showing the NDVIs of 2023(left) and 2020(right):

<p align="center">
  <img src="https://github.com/Christobaltobbin/Drought_Assessment/assets/116877317/3a657b2b-8233-4451-9f61-1a46f0f2b4ad.png" align="left" width="385" height="250">
  <img src="https://github.com/Christobaltobbin/Drought_Assessment/assets/116877317/47e25118-c89b-49f7-8534-a9e0e0caef81.png" align="right" width="385" height="250">
</p>


Below are the LAI histograms for 2023(left) and 2020(right):

<p align="center">
  <img src="https://github.com/Christobaltobbin/Drought_Assessment/assets/116877317/4dd6b76e-a2e0-4f4b-bd41-65d56fcb6977.png" align="left" width="385" height="250">
  <img src="https://github.com/Christobaltobbin/Drought_Assessment/assets/116877317/fba1737d-54e1-45e7-bdab-e8c72259030a.png" align="right" width="385" height="250">
</p>

## Conclusion
The results from the study shows that there has been a reduction in vegeation density and health in Janga from 2020 to 2023.
