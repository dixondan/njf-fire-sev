Last updated: 01.2022 

Overview
--------

This repository is associated with the [open access paper](https://www.sciencedirect.com/science/article/pii/S0034425721005836, "Fire Severity in NJF")
 "Regional-scale fire severity mapping of *Eucalyptus* forests with the Landsat archive" in the journal *Remote Sensing of Environment* by Dan Dixon, Nik Callow, John Duncan, Sam Setterfield, and Natasha Paul (2022). 

<p align="center">
  <img src="figs/graph-abs2.png" />
</p>

Earth Engine App: Visualise fire severity
--------
[A Google Earth Engine application](https://danieljdixon1991.users.earthengine.app/view/njf-fire-sev-app "njf-fire-sev-app") is available to visualise predicted fire severity on prescribed burns and wildfires from 2005 to 2020 in the Northern Jarrah Forest of Western Australia. 

<p align="center">
  <img src="figs/app-demo.gif" />
</p>

Data
--------
  - Download predicted fire severity rasters for each fire at 30 x 30 m resolution
  - Shapefile to associate each predicted raster and burn perimeter
  - Dates-of-fire obtained from MODIS (CSV)
 
Analyse
--------
   -  Calculate the areas of predicted fire severity in Table 3 (calculate_areas_ee.ipynb)
   -  Compute the severity of the Wooroloo bushfire from 2021 (or any given fire of interest) (predict_my_fire.ipynb)

Cite
--------
Dan J. Dixon, J. Nikolaus Callow, John M.A. Duncan, Samantha A. Setterfield, Natasha Pauli,
Regional-scale fire severity mapping of Eucalyptus forests with the Landsat archive,
Remote Sensing of Environment, Volume 270, 2022, 112863, ISSN 0034-4257,
https://doi.org/10.1016/j.rse.2021.112863.

Questions
--------
Dan J. Dixon

Email: 1dandixon@gmail.com
Cooperative Research Centre for Honeybee Products: https://www.crchoneybeeproducts.com/
