Last updated: 01.2022 

Overview
--------

This repository is associated with the paper "Regional-scale fire severity mapping of *Eucalyptus* forests with the Landsat archive" in the journal *Remote Sensing of Environment* from 2022. 

![This is an image](figs/graph-abs-wlogos2.png)
<img src="figs/graph-abs-wlogos2.png" width="50" height="50">


Visualise fire severity
--------
A Google Earth Engine application to visualise predicted fire severity on prescribed burns and wildfires from 2005 to 2020 in the Northern Jarrah Forest (link)


Data
--------

  - Direct download predicted fire severity rasters for each fire at 30 x 30 m resolution
  - Shapefile to associate each predicted raster and burn perimeter
  - Tables containing the following:
    - Train/test fire info -> predictors and response variable for training random forest (CSV)
    - Dates-of-fire obtained from MODIS (CSV)
 
Analyse
--------
   -  Accessing fire data through Earth Engine image collection + Explore, plot and map a fire 
   -  Apply the model to your own fire polygon (In progress)



