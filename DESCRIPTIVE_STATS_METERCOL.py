# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 16:56:03 2021

@author: Admin
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

import seaborn as sns

#cambiar la ruta en donde esta el dataset
Datos_metercol="C:\\Users\\Admin\\Downloads\\MeterCOL\\"

metercol=pd.read_csv(Datos_metercol+"MeteorCOLUnited.csv", sep=",")

descdf=metercol.describe()
#format two decimals:
pd.options.display.float_format = "{:,.2f}".format

#export tabla descriptive stats en formato csv
descdf.to_csv(Datos_metercol+'descriptive_stats_metercol.csv')

#################################################################

#grafico de distribucion y kde por variable de interes.
variables=['DHI','DNI','GHI', 'Clearsky DHI', 'Clearsky DNI', 'Clearsky GHI','Wind Speed', 'Precipitable Water', 
           'Wind Direction',
       'Relative Humidity', 'Temperature', 'Pressure',
       'Global Horizontal UV Irradiance (280-400nm)',
       'Global Horizontal UV Irradiance (295-385nm)']
variables1=['DHI']

#no me funciono el for del export de varibas graficas , falta revisar el plt.savefig
for i in variables1:
    var='Surface Albedo'
    
    #export de la figura en la carpeta de los datos
    plt.savefig(Datos_metercol+"Histograma_KDE_P[0,100]_"+var+".png",dpi=300)
    #plt.figure.clear()
    #quitando valores extremos. Aqui de acuerdo a los valores de las estadisticas descriptivas, toman los valores omitiendo valores por debajo del percentil 1 y por encima del percentil 95 (valores extremos)
    metercol1=metercol[(metercol[var]<metercol[var].quantile(.99)) & (metercol[var]>metercol[var].quantile(.01))]
    hist_kde_ext=sns.histplot(data=metercol1, x=var,kde=True).set(title='Histogram and KDE '+var+' P[1,99]')
    plt.savefig(Datos_metercol+"Histograma_KDE_"+var+".png",dpi=300)