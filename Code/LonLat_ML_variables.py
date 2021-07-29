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
print("Imports done")
data_path='/home/bleon/Documents/DS4A/DS4A_Project/Processed_Data'
Export_path='/home/bleon/Documents/DS4A/DS4A_Project/Code/ExportData'
ts1=datetime.datetime.now().timestamp()

Var_No=7
Year=2011
Variables_ToPlot=["DHI","DNI","GHI","Dew Point","Surface Albedo","Precipitable Water","Relative Humidity","Temperature","Pressure","Wind Speed"]

Coordinate_List=[
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
DF=pd.read_csv(data_path+"/LocationYearAverage.csv",usecols=Variables_ToPlot+["Year","Longitude","Latitude"])
DF=DF[DF["Year"]==Year]
LonLatVar={}
for var in Variables_ToPlot:
    LonLatVar[var]=list(zip(DF["Longitude"],DF["Latitude"],DF[var]))
# DF=DF[DF["Year"]==Year]

def valor(coords,var):
    distlon=[]
    distlat=[]
    valor=[]
    for vals in LonLatVar[var]:
        distlon.append((coords[0]-vals[0])**2)
        distlat.append((coords[1]-vals[1])**2)
        valor.append(vals[2])
    NewDist=1.0/np.sqrt(np.array(distlon)+np.array(distlat))
    Sum_up=np.sum(NewDist*np.array(valor))
    Sum_down=np.sum(NewDist)
    return Sum_up/Sum_down

def extractLon(coords):
    return coords[0]
def extractLat(coords):
    return coords[1]


coordenadas=[[(j,i) for i in np.arange(min(longitude),max(longitude),0.1)] for j in np.arange(min(latitude)-5,max(latitude)+5,0.1)]
# coordenadas=[[(round(j,2),round(i,2)) for i in np.linspace(min(longitude),max(longitude),num=100)] for j in np.linspace(min(latitude)-5,max(latitude)+5,num=100)]
Lista_coords=[]
for list in coordenadas:
    Lista_coords+=list
    
New_Values=pd.DataFrame({"Coordenadas":Lista_coords})
for var in Variables_ToPlot:
    New_Values[var]=New_Values["Coordenadas"].apply(valor,args=(var,))
New_Values["Longitude"]=New_Values["Coordenadas"].apply(extractLon)
New_Values["Latitude"]=New_Values["Coordenadas"].apply(extractLat)
print(New_Values.head(10))
New_Values.to_csv(Export_path+"/HeatData/AllVariables_HeatData.csv")
ts2=datetime.datetime.now().timestamp()
print("Script done in {} seconds".format(ts2-ts1))