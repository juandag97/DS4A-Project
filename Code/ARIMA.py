#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ARIMA forecasting for different variable and location
""" 
#Imports
import datetime
ts1=datetime.datetime.now().timestamp()
import numpy as np
import matplotlib.pylab as plt
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import warnings
warnings.filterwarnings('ignore', 'statsmodels.tsa.arima_model.ARMA',
                        FutureWarning)
warnings.filterwarnings('ignore', 'statsmodels.tsa.arima_model.ARIMA',
                        FutureWarning)
print("Imports done")


#Data import and grouping
data_path="/home/bleon/Documents/DS4A/DS4A_Project/Processed_Data/"

CompleteDF=pd.read_csv(data_path+"MeteorCOLUnited.csv",usecols=["Year","Month","Day","Hour","Minute","Wind Speed","GHI","Temperature","Latitude","Longitude"])
CompleteDF["datetime"]=pd.to_datetime(CompleteDF["Year"].astype("str")+"-"+CompleteDF["Month"].astype("str")+"-"+CompleteDF["Day"].astype("str")+" "+CompleteDF["Hour"].astype("str")+":"+CompleteDF["Minute"].astype("str")+":00")
CompleteDF["Coords"]=list(zip(CompleteDF["Latitude"],CompleteDF["Longitude"]))

print("Data done")
#Columns= Year  Month  Day  Hour  Minute  GHI  Wind Speed  Temperature  Latitude  Longitude Coords datetime


#Inputs
# User must imput CoordNo which indicates which location to forecast and VarNo to chose among Temperature, GHI and Wind Speed 
Variables_to_forecast=["Temperature","GHI","Wind Speed"]
AllCoords=CompleteDF["Coords"].unique().tolist()
VarNo=0
CoordNo=2
Variable=Variables_to_forecast[VarNo]
Location=AllCoords[CoordNo]
DF=CompleteDF[CompleteDF["Coords"]==Location][["Year","Month","Coords",Variable,"datetime"]].groupby(["Year","Month","Coords"]).mean().reset_index()
DF["datetime"]=pd.to_datetime(DF["Year"].astype("str")+"-"+DF["Month"].astype("str")+"-01")
DF.head(5)
print("Location chosen - coordinates= {}".format(Location))
print("Variable to forecast: {}".format(Variable))

#ARIMA Model fitting with parameters
def ArimaForecast(loca,vari,ARp=1,Id=1,MAq=1,SEs=12):
    """Function that returns training data with informtion and forecasted variable

    Args:
        loca (tuple): Latitude and Longitude tuple found from CompleteDF
        vari (str): Name of variable to forecast, can be Temperature, GHI, Wind Speed
        ARp (int, optional): Order of autoregresive component of SARIMA. Defaults to 1.
        Id (int, optional): Order of integrated component in SARIMA. Defaults to 2.
        MAq (int, optional): Order of moving average component in SARIMA. Defaults to 1.
        SEs (int, optional): Order of seasonal component of SARIMA. Defaults to 12 (yearly)

    Returns:
        MyData (dictionary): Dictionary containing data series,time stamp, location, variable and AIC value of fitted model
        MyForecast (dictionary): Dictionary containing forecasted values and dates for 2 years
    """    
    NewDF=CompleteDF[CompleteDF["Coords"]==loca][CompleteDF["Year"]<=2020][["Year","Month","Coords",vari,"datetime"]].groupby(["Year","Month","Coords"]).mean().reset_index()
    NewDF["datetime"]=pd.to_datetime(NewDF["Year"].astype("str")+"-"+NewDF["Month"].astype("str")+"-01")
    TimeSeries=NewDF[vari]
    TimeSeries_dates=NewDF["datetime"]
    TheModel_fitted=ARIMA(TimeSeries,seasonal_order=(ARp,Id,MAq,SEs))
    
    NewForecast=pd.Series(TheModel_fitted.forecast(24, alpha=0.05)).tolist()
    NewForecast_dates=pd.to_datetime(pd.Series(["2021-"+str(i+1)+"-01" for i in range(12)]+["2020-"+str(i+1)+"-01" for i in range(12)])).tolist()
    
    MyForecast={"Location":loca,"Variable":vari,"Values":NewForecast,"datetime":NewForecast_dates,"AIC":TheModel_fitted.aic}
    MyData={"Location":loca,"Variable":vari,"Values":TimeSeries,"datetime":TimeSeries_dates}
    return MyData,MyForecast



ts2=datetime.datetime.now().timestamp()
print("Running script took {} seconds".format(ts2-ts1))
