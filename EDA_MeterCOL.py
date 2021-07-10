#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module documentation goes here
and here
   and ...
""" 
import numpy as np
import matplotlib.pylab as plt
import datetime
import pandas as pd
import pathlib
path=str(pathlib.Path(__file__).parent.absolute())
ts1=datetime.datetime.now().timestamp()

start=datetime.datetime.now().timestamp()
path=str(pathlib.Path(__file__).parent.absolute())
data_path='/home/bleon/Documents/DS4A/DS4A_Project/Procesed_Data/'
plt.style.use('ggplot')
print("Imports done")

DF_COL=pd.read_csv(data_path+"MeteorCOLUnited.csv")
DF_COL["Datetime"]=DF_COL["Year"].astype("str")+"-"+DF_COL["Month"].astype("str")+"-"+DF_COL["Day"].astype("str")+" "+DF_COL["Hour"].astype("str")+":"+DF_COL["Minute"].astype("str")+":00"

