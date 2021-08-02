#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ARIMA forecasting for different 
""" 
#Imports
import datetime
ts1=datetime.datetime.now().timestamp()
import numpy as np
import matplotlib.pylab as plt
import pandas as pd
import pathlib
# from statsmodels.tsa.arima_model import ARIMA
# from pyramid.arima import auto_arima

#Inputs
VarNo=0
CoordNo=0
print("Imports done")

#Data import and grouping
path=str(pathlib.Path(__file__).parent.absolute())
data_path="/home/bleon/Documents/DS4A/DS4A_Project/Processed_Data/"

CompleteDF=pd.read_csv(data_path+"MeteorCOLUnited.csv",usecols=["Year","Month","Day","Hour","Minute","Wind Speed","GHI","Temperature","Latitude","Longitude"])
CompleteDF["datetime"]=pd.to_datetime(CompleteDF["Year"].astype("str")+"-"+CompleteDF["Month"].astype("str")+"-"+CompleteDF["Day"].astype("str")+" "+CompleteDF["Hour"].astype("str")+":"+CompleteDF["Minute"].astype("str")+":00")
CompleteDF["Coords"]=list(zip(CompleteDF["Latitude"],CompleteDF["Longitude"]))

Variables_to_forecast=["Temperature","GHI","Wind SPeed"]
AllCoords=CompleteDF["Coords"].unique().tolist()
Variable=Variables_to_forecast[VarNo]
Location=AllCoords[CoordNo]
print("Data done")
#Columns= Year  Month  Day  Hour  Minute  GHI  Wind Speed  Temperature  Latitude  Longitude Coords datetime
#To forecast monthly data we will take monthly data for every variable for a station untill 2019 and forecast 2020 as testing data

#From Autocorrelation script we find that p=2 d>=3 q=3
#Testing on first latitude
print("Location chosen - coordinates= {}".format(Location))
print("Variable to forecast: {}".format(Variable))

DF=CompleteDF[CompleteDF["Coords"]==Location]["Year","Month",Location,Variable,"datetime"].groupby(["Year","Month",Location]).mean()
fig=plt.figure()
DF[Variable].plot()
plt.show()


ts2=datetime.datetime.now().timestamp()
print("Running script took {} seconds".format(ts2-ts1))
