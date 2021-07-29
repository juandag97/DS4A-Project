#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Joining files for organized data 
""" 
#%% Importing modules

# import numpy as np
# import matplotlib.pylab as plt
import datetime
import pandas as pd
import pathlib
import glob
from tqdm import tqdm
import gc
#%% Histload data
working_path=str(pathlib.Path(__file__).parent.absolute())
start=datetime.datetime.now().timestamp()
print("Script working from:" + working_path)
Histload_paths=working_path+'/../Raw_Data/*/*'
globs=glob.glob(Histload_paths)
histloads=[]
for item in globs:
    if "/HistLoad" in item:
        histloads.append(item)
HistDict={}
print("Generating dictionary with dataframes for every Histload File")
for k in tqdm(range(len(histloads))):
    HistDict["data"+str(k)]=pd.read_csv(histloads[k],delimiter=",")

DF_hist=pd.concat(HistDict.values(),ignore_index=True)
DF_hist["Time"]=pd.to_datetime(DF_hist["Time Stamp"])
print("Time to generate dataframe with all histload data = {} minutes".format((datetime.datetime.now().timestamp()-start)/60.0))
DF_hist.to_csv(working_path+'/../Procesed_Data/HistLoadUnited.csv')
del DF_hist
for k in range(len(histloads)):
    del HistDict["data"+str(k)]
del HistDict
gc.collect()
print("Exporting and deleting done")
#Columns= [Time Stamp,Time Zone,Name,PTID,Load,Time]
#%% Meteorologic data
start2=datetime.datetime.now().timestamp()
Meteorol_path=working_path+'/../Raw_Data/Datos_Meteorologicos/*'
meteoro=glob.glob(Meteorol_path)
MetDict={}
print("Generating dictionary with dataframes for every meteorologic data File")
for k in tqdm(range(len(meteoro))):
    MetDict["data"+str(k)]=pd.read_csv(meteoro[k],delimiter=",",skiprows=2)
    MetDict["data"+str(k)]["File"]=meteoro[k].replace(working_path+'/../Raw_Data/Datos_Meteorologicos/', "").replace(".csv","")
DF_Met=pd.concat(MetDict.values(),ignore_index=True)
print("Time to generate dataframe with all meteorologic data 1 = {} minutes".format((datetime.datetime.now().timestamp()-start2)/60.0))
DF_Met.to_csv(working_path+'/../Procesed_Data/MeteorUnited.csv')
del DF_Met
for k in range(len(meteoro)):
    del MetDict["data"+str(k)]
del MetDict
gc.collect()
print("Exporting and deleting done")
#%% Meteorologic data 2
start3=datetime.datetime.now().timestamp()
Meteorol_path2=working_path+'/../Raw_Data/Datos_Meteorologicos2/*.csv'
Meteorol_path3=working_path+'/../Raw_Data/Datos_Meteorologicos3/*/*.csv'
meteoro2=glob.glob(Meteorol_path2)
meteoro3=glob.glob(Meteorol_path3)
meteoroCOL=meteoro2+meteoro3
MetDict2={}
print("Generating dictionary with dataframes for every meteorologic data File from second set")
# for k in tqdm(range(len(meteoroCOL))):
for k in range(len(meteoroCOL)):
    a=pd.read_csv(meteoroCOL[k],delimiter=",",skiprows=2)
    if a["Year"].max()>1998:
        MetDict2["data"+str(k)]=a[a["Year"]>=1999].copy()
        print(meteoroCOL[k].replace(working_path,"").replace('/../Raw_Data/Datos_Meteorologicos', "").replace(".csv","")[-24:].split("_"))
        MetDict2["data"+str(k)]["File"]=meteoroCOL[k].replace(working_path,"").replace('/../Raw_Data/Datos_Meteorologicos', "").replace(".csv","")
        MetDict2["data"+str(k)][["File","Latitude","Longitude","Year"]]=MetDict2["data"+str(k)]["File"].str[-24:].str.rsplit("_",expand=True,n=3)
        # MetDict2["data"+str(k)][["File","Latitude","Longitude","Year"]]=meteoroCOL[k].replace(working_path,"").replace('/../Raw_Data/Datos_Meteorologicos', "").replace(".csv","")[-24:].split("_")
        print(meteoroCOL[k]+" Done!")
    else:
        print(meteoroCOL[k] + " is before 1998")
    
DF_Met2=pd.concat(MetDict2.values(),ignore_index=True)
print("Shape of Colombia meteorologic data:")
print(DF_Met2.shape)
print("Time to generate dataframe with all meteorologic data from Colombia = {} minutes".format((datetime.datetime.now().timestamp()-start3)/60.0))
DF_Met2.to_csv(working_path+'/../Procesed_Data/MeteorCOLUnited.csv')
del DF_Met2
del MetDict2
gc.collect()
print("Exporting and deleting done")
#%% Consumption data
start4=datetime.datetime.now().timestamp()
Residence_path=working_path+'/../Raw_Data/044b38-JFP-20210315-20-58-1H.csv'
DF_Res=pd.read_csv(Residence_path)
DF_Res.to_csv(working_path+'/../Procesed_Data/ResidencesUnited.csv')
print("Time to generate dataframe with residence data = {} minutes".format((datetime.datetime.now().timestamp()-start4)/60.0))



print("Time to run scrpt = {} minutes".format((datetime.datetime.now().timestamp()-start)/60.0))
