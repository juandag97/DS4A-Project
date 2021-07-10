#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Guarda figura con las 9 variables puestas en *Variables_ToPlot* para el año *year*.
Toca poner el path en *data_path* a donde esta guardado el csv MeteorCOLUnited.
Figura se guarda en el mismo directorio de donde esta guardado corre el script.

""" 
import numpy as np
import matplotlib.pylab as plt
import datetime
import pandas as pd
import pathlib
import seaborn as sns
from tqdm import tqdm
path=str(pathlib.Path(__file__).parent.absolute())
ts1=datetime.datetime.now().timestamp()
start=datetime.datetime.now().timestamp()

data_path='/home/bleon/Documents/DS4A/DS4A_Project/Procesed_Data/'
plt.style.use('ggplot')
print("Imports done")

Variables_ToPlot=["DHI","DNI","GHI","Dew Point","Surface Albedo","Precipitable Water","Relative Humidity","Temperature","Pressure"]
Variables_types=["float32","float32","float32","float32","float32","float32","float32","float32","float32"]
Types_dict=dict(zip(Variables_ToPlot,Variables_types))
year=2016

#Importa csv
DF_COL=pd.read_csv(data_path+"MeteorCOLUnited.csv",usecols=Variables_ToPlot+["Year","Month","Day","Hour","Minute","Latitude","Longitude"])
#Crea varible datetime
# DF_COL["Datetime"]=pd.to_datetime(DF_COL["Year"].astype("str")+"-"+DF_COL["Month"].astype("str")+"-"+DF_COL["Day"].astype("str")+" "+DF_COL["Hour"].astype("str")+":"+DF_COL["Minute"].astype("str")+":00")

#Cambia 
DF_COL.astype(Types_dict)
print("DF_COL imported with columns and dtypes:")
print(DF_COL.dtypes)

#Selecciona forma de agregacion de las variables 
variables_functions=[np.mean,np.mean,np.mean,np.mean,np.mean,np.mean,np.mean,np.mean,np.mean]
variable_agg=dict(zip(Variables_ToPlot,variables_functions))
DF_plot=DF_COL[DF_COL["Year"]==year][Variables_ToPlot+["Year","Month","Day","Latitude","Longitude"]].groupby(["Year","Month","Day","Latitude","Longitude"]).agg(variable_agg).reset_index()
DF_plot["Datetime"]=pd.to_datetime(DF_plot[["Year","Month","Day"]])

def plot_series(DF,serie,axis):
    """Returns  a seaborn lineplot from the selected dataframe grouped by Latitude for the year stated and the selected column

    Args:
        DF (Dataframe): Dataframe to use
        serie (str): Name of variable in DF to plot
        axis (matplotlib.axis): axis in generated matplotlib.axes 

    Returns:
        sns.lineplot: Lineplot separated by latitude of sensor through selected year
    """        
    # print("generating plot for year {} and variable {}".format(year,serie))
    LinePlot=sns.lineplot(data=DF,y=serie,x="Datetime",hue="Latitude",ax=axis,legend=False,ci=None)
    LinePlot.set_xticklabels(labels=["Ene","Mar","May","Jul","Sep","Nov"],rotation=30)
    axis.set_ylabel(serie,size="x-small")
    axis.set_xlabel("Datetime",size="xx-small")
    
    return LinePlot

#Generates plot
print("Plotting variables for year {}".format(year))
fig,(axes)=plt.subplots(len(Variables_ToPlot),1,sharex=True)
newaxes=axes.flatten()
for k in tqdm(range(9)):
    _=plot_series(DF_plot,Variables_ToPlot[k],newaxes[k])
plt.suptitle("Variables for year {}".format(year))
fig.set_size_inches(5, 1.5*len(Variables_ToPlot))
plt.tight_layout()
plt.savefig(path+"/EDA_variables_{}.png".format(year))

print("Script corre en {} minutos".format((datetime.datetime.now().timestamp()-start)/60))



    


    

