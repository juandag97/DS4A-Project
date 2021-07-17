#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Leon - DS4A cohort 5
"""
Script generates folium html map with markers on meteorology station locations
Coordinate list may be updated to include more stations
Data from LocationYearAverage creates data per year per station for custom heatmap
""" 
import numpy as np
import matplotlib.pylab as plt
import datetime
import pandas as pd
import pathlib
import folium 
from folium.plugins import HeatMap

data_path='/home/bleon/Documents/DS4A/DS4A_Project/Procesed_Data/'
Heat_layer=False
path=str(pathlib.Path(__file__).parent.absolute())
ts1=datetime.datetime.now().timestamp()
Coordinate_List=[
    # (18.29,-67.34),
    # (18.21,-67.14),
    # (18.49,-67.14),
    # (18.45,-66.18),
    (10.41,-75.58),
    (4.29,-74.82),
    (9.73,-75.06),
    (10.97,-73.54),
    (9.73,-73.86),
    (11.33,-72.74),
    (8.53,-76.70),
    (8.05,-75.18),
    (8.77,-75.86),
    (10.69,-74.86),
    (10.49,-74.34),
    (10.41,-75.58),
    (8.93,-75.46),
    (8.21,-76.38),
    (9.17,-75.30),
    (7.85,-76.82),
    (6.73,-76.70),
    (10.77,-73.98),
    (8.37,-74.90),
    (7.33,-75.78),
    (9.05,-74.10),
    (4.29,-74.82),
    (10.45,-73.18),
    (10.21,-74.90)
]
longitude=[tup[0] for tup in Coordinate_List]
latitude=[tup[1] for tup in Coordinate_List]
CoordinatesDF=pd.DataFrame({"longitude":longitude,"latitude":latitude})
Variable=pd.read_csv(data_path+"/LocationYearAverage.csv")


map=folium.Map(location=(9.00,-75.00),zoom_start=6
            #    ,tiles=
            #    "Stamen Toner"
            #    "Stamen Terrain"
            #    "cartodbpositron"
               )

if Heat_layer:
    Heat_info=zip(latitude,longitude,Variable)
    hm_layer = HeatMap(Heat_info,
                   # These are parameters that we tweak manually to adjust color
                   # See folium docs for more information
                   min_opacity=0.2,
                   radius=8,
                   blur=6, 
                 )
    map.save(path+"/HeatMap.html")
else:
    for tup in Coordinate_List:
        folium.Marker(location=tup).add_to(map)
    map.save(path+"/CodeStation_Locations.html")
