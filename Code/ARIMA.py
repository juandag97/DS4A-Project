#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ARIMA forecasting for different variables and locations, set to forecast 24 months from january 2021
input:MeteorCOLUnited.csv
output: forecasted_24Months.csv
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
# VarNo=0
# CoordNo=2
# Variable=Variables_to_forecast[VarNo]
# Location=AllCoords[CoordNo]
DF=CompleteDF[["Year","Month","Coords"]+Variables_to_forecast].groupby(["Year","Month","Coords"]).mean().reset_index()
DF["datetime"]=pd.to_datetime(DF["Year"].astype("str")+"-"+DF["Month"].astype("str")+"-01")


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
    NewDF=CompleteDF[CompleteDF["Coords"]==loca][["Year","Month","Coords",vari]]
    NewDF=NewDF[NewDF["Year"]<=2020].groupby(["Year","Month","Coords"]).mean().reset_index()
    print(NewDF.head(3))
    NewDF["datetime"]=pd.to_datetime(NewDF["Year"].astype("str")+"-"+NewDF["Month"].astype("str")+"-01")
    TimeSeries=NewDF[vari]
    TimeSeries_dates=NewDF["datetime"]
    TheModel_fitted=ARIMA(TimeSeries,order=(2,2,1),seasonal_order=(ARp,Id,MAq,SEs)).fit()
    NewForecast=pd.Series(TheModel_fitted.forecast(24, alpha=0.05)).tolist()
    NewForecast_dates=pd.to_datetime(pd.Series(["2021-"+str(i+1)+"-01" for i in range(12)]+["2020-"+str(i+1)+"-01" for i in range(12)])).tolist()
    
    MyForecast={"Location":[loca for n in range(len(NewForecast_dates))],"Variable":[vari for n in range(len(NewForecast_dates))],"Values":NewForecast,"datetime":NewForecast_dates,"AIC":[TheModel_fitted.aic for n in range(len(NewForecast_dates))]}
    MyData={"Location":loca,"Variable":vari,"Values":TimeSeries,"datetime":TimeSeries_dates}
    return MyData,MyForecast

forecasted=pd.DataFrame({"Location":[],"Variable":[],"Values":[],"datetime":[],"AIC":[]})
for loc in AllCoords:
    for var in Variables_to_forecast:
        _,NewDF=ArimaForecast(loca=loc,vari=var)
        forecasted=pd.concat([pd.DataFrame(NewDF),forecasted],ignore_index=True)
        print("Variable {} and location {} forecast done after {} seconds".format(var,loc,datetime.datetime.now().timestamp()-ts1))
print(forecasted.head(10))   
print(forecasted.describe())
GHI=forecasted[forecasted["Variable"]=="GHI"]
Wind=forecasted[forecasted["Variable"]=="Wind Speed"]
Temp=forecasted[forecasted["Variable"]=="Temperature"]
# forecasted.to_csv(data_path+"ARIMA_24Months.csv")

from sklearn.linear_model import LinearRegression


Wind_gen=pd.read_csv(data_path+'WindSpeed.csv')
GHI_gen=pd.read_csv(data_path+'GHI_generation.csv')
Xg,yg=GHI_gen[["GHI"]],GHI_gen["MAX"]
model_GHI=LinearRegression().fit(Xg,yg)

Wind_gen["WindSquared"]=Wind_gen["WindSpeed"].apply(lambda x:x**2)
Xw,yw=Wind_gen[["WindSquared","WindSpeed"]],Wind_gen["MAX"]
model_Wind=LinearRegression().fit(Xw,yw)

IntGHI,COEFGHI=model_GHI.intercept_ , model_GHI.coef_[0]
IntWind,COEFWIND,COEFWIND2=model_Wind.intercept_ , model_Wind.coef_[0], model_Wind.coef_[1]
def Wind_real_generation(x):
    return IntWind+COEFWIND*(x**2)+COEFWIND2*(x)
def Solar_real_generation(x):
    return IntGHI+COEFGHI*x

Wind["Values"]=Wind["Values"].apply(Wind_real_generation)
GHI["Values"]=GHI["Values"].apply(Solar_real_generation)

ForecastedEnergy=pd.concat([Wind,GHI])

# Wind.to_csv(data_path+"ARIMA_Wind_Forecast.csv")
# GHI.to_csv(data_path+"ARIMA_GHI_Forecast.csv")
ForecastedEnergy.to_csv(data_path+"ARIMAEnergy_24months.csv")


ts2=datetime.datetime.now().timestamp()
print("Running script took {} seconds".format(ts2-ts1))
