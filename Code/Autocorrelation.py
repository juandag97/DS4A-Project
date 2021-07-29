#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Plots autocorrelation and partial autocorrelation for a chosen location and variable
""" 

import numpy as np
import matplotlib.pylab as plt
import datetime
import pandas as pd
import pathlib
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.graphics.tsaplots import plot_acf

print("Imports done")
path=str(pathlib.Path(__file__).parent.absolute())
ts1=datetime.datetime.now().timestamp()
LonLatNum=0 #Choose number of appearance of Longitude-Latitude tuple to plot autocorrelation at that station
VarNum=9    #Choose variable number from the list Variables_ToPlot
data_path='/home/bleon/Documents/DS4A/DS4A_Project/Processed_Data/'
Export_path='/home/bleon/Documents/DS4A/DS4A_Project/Code/ExportData/'
plt.style.use('ggplot')

Variables_ToPlot=["DHI","DNI","GHI","Dew Point","Surface Albedo","Precipitable Water","Relative Humidity","Temperature","Pressure","Wind Speed"]
Variables_types=["float32","float32","float32","float32","float32","float32","float32","float32","float32"]
Types_dict=dict(zip(Variables_ToPlot,Variables_types))


#Importa csv creado por DAataJoin.py
DF_COL=pd.read_csv(data_path+"MeteorCOLUnited.csv",usecols=Variables_ToPlot+["Year","Month","Day","Hour","Minute","Latitude","Longitude"])
#Cambia dtypes de cada columna
DF_COL.astype(Types_dict) 
print("Data import done")

DF_COL["To_Month"]=DF_COL["Year"].astype("str")+"-"+DF_COL["Month"].astype("str")
DF_COL["To_Day"]=DF_COL["Year"].astype("str")+"-"+DF_COL["Month"].astype("str")+"-"+DF_COL["Day"].astype("str")
DF_COL["LonLat"]=list(zip(DF_COL["Longitude"],DF_COL["Latitude"]))
New_DF=DF_COL.groupby(["LonLat","To_Month"]).mean().reset_index()
print("Grouped DF done")
LonLatValues=New_DF["LonLat"].unique().tolist()

#Autocorrelation
series=New_DF[New_DF["LonLat"]==LonLatValues[LonLatNum]][Variables_ToPlot[VarNum]]
fig,(axes1,axes2)=plt.subplots(2,1,sharex=True)
axes2.set_xlabel("lags")
# print(type(LonLatValues[LonLatNum]))
# plt.suptitle(Variables_ToPlot[VarNum]+" with lags of 1 month ")
plt.suptitle(Variables_ToPlot[VarNum]+" with lags of 1 month "+" at location {}".format(str(LonLatValues[LonLatNum])))

# autocorrelation_plot(series)
plot_acf(series,lags=50,ax=axes1)
plot_pacf(series,lags=50,ax=axes2)
plt.tight_layout()
ts2=datetime.datetime.now().timestamp()
plt.savefig(Export_path+"Autocorrelation/"+Variables_ToPlot[VarNum]+"_PACF_ACF.png") 
print("time to run script and save figure ={} seconds".format(ts2-ts1))
# plt.show()