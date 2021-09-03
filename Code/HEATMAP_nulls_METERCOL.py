# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 11:29:49 2021

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
  
#isntalar  missingno
#!pip install missingno==0.5.0 

import missingno as msno

#Grafico total del conjunto de datos
%matplotlib inline
msno.matrix(metercol)

#grafico alternativo, de heatmap
msno.heatmap(meterco)


#esta parte es si se quiere graficar para determinados periodos:
#Grafico de missing por anho-mes. Primero se debe crear la variable en date()
#metercol['Datef']=metercol['Year'].astype(str)+'-'+metercol['Month'].astype(str)+'-01'
#metercol['Datef']=metercol['Datef'].map(lambda x: datetime.strptime(x, '%Y-%m-%d').date())

#%matplotlib inline
#msno.matrix(metercol.set_index(pd.period_range('2005-01-01', '2020-01-01', freq='Y')) , freq='Year')