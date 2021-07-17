#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Benjamin Leon - DS4A cohort 5
"""
Script generates average of chosen variable per year per location
Plots the results as yearly average
Saves in csv
""" 
import numpy as np
import matplotlib.pylab as plt
import datetime
import pandas as pd 
import pathlib
import seaborn as sns
working_path=str(pathlib.Path(__file__).parent.absolute())
start=datetime.datetime.now().timestamp()
data_path='/home/bleon/Documents/DS4A/DS4A_Project/Procesed_Data/'
Var_No=1
plt.style.use('ggplot')
print("Imports done")

Variables_ToPlot=["DHI","DNI","GHI","Dew Point","Surface Albedo","Precipitable Water","Relative Humidity","Temperature","Pressure"]
Variables_types=["float32","float32","float32","float32","float32","float32","float32","float32","float32"]
Types_dict=dict(zip(Variables_ToPlot,Variables_types))


#Importa csv creado por DAataJoin.py
DF_COL=pd.read_csv(data_path+"MeteorCOLUnited.csv",usecols=Variables_ToPlot+["Year","Month","Day","Hour","Minute","Latitude","Longitude"])

#Cambia dtypes de cada columna
DF_COL.astype(Types_dict) 


DF_COL["Longitude-Latitude"]=list(zip(DF_COL["Latitude"],DF_COL["Longitude"]))


DF_grouped=DF_COL.groupby(["Year","Longitude","Latitude","Longitude-Latitude"]).mean().reset_index()
stop=datetime.datetime.now().timestamp()
print("Groupby done after {} seconds".format(start-stop))

def YearMeanFig(Var):
    plt.figure(figsize=(14,5))
    sns.barplot(x="Year",y=Variables_ToPlot[Var],data=DF_grouped,hue="Longitude-Latitude",ci=None)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
    plt.tight_layout()
    plt.ylabel(Variables_ToPlot[Var])
    plt.xlabel("Year")
    plt.savefig(working_path+"/ExportData/"+Variables_ToPlot[Var]+"_year_mean.png")
stop1=datetime.datetime.now().timestamp()

## Activar o desactivar esta linea (y desactivar el for) para graficar una unica variable
for i in range (len(Variables_ToPlot)):
    YearMeanFig(i)
    print(Variables_ToPlot[i]+" figure done!")
# YearMeanFig(Var_No)

print("Figs done after {} seconds".format(start-stop1))   

##Activar o desactiar esta parte para guardar o no guardar el dataset que se utiliza en el script Map_Data.py
DF_grouped.to_csv(data_path+"/LocationYearAverage.csv")
stop2=datetime.datetime.now().timestamp()
print("Data done after {} seconds".format(start-stop2))



