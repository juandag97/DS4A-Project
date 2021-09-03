#%%
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Exploratory data analysis for source data report DS4A
""" 

import numpy as np
import matplotlib.pylab as plt
import datetime
import pandas as pd
import pathlib
import seaborn as sns 
from tqdm import tqdm
start=datetime.datetime.now().timestamp()
path=str(pathlib.Path(__file__).parent.absolute())
data_path='/home/bleon/Documents/DS4A/DS4A_Project/Procesed_Data/'
plt.style.use('ggplot')
print("Imports done")

#%% HistLoad
DF_hist=pd.read_csv(data_path+"HistLoadUnited.csv",usecols=["Time Stamp","Name","PTID","Load"])
DF_hist["Time Stamp"]=pd.to_datetime(DF_hist["Time Stamp"])
DF_hist["Name"]=DF_hist["Name"].astype("str")
print("DF_hist imported")

fig,(axes)=plt.subplots(2,1,sharey=True)
plt.xticks(rotation=30)
a=sns.lineplot(data=DF_hist[DF_hist["Time Stamp"]>datetime.datetime(2019, 1, 1)],x="Time Stamp",y="Load",hue="Name",ax=axes[0],legend=False)
plt.xticks(rotation=30)
b=sns.lineplot(data=DF_hist[DF_hist["Time Stamp"]<datetime.datetime(2019, 1, 1)],x="Time Stamp",y="Load",hue="Name",ax=axes[1],legend=False)
axes[0].set_ylabel("Load",size="x-small")
axes[1].set_ylabel("Load",size="x-small")
axes[0].set_xlabel("",size="x-small")
axes[1].set_xlabel("Date",size="x-small")
plt.xticks(rotation=30)
# axes[0].set_xticklabels(rotation=45)
# axes[1].set_xticklabels(rotation=45)
plt.tight_layout()
plt.suptitle("Histloads")
plt.savefig(path+"/HistLoad.png")
print("Histload plot done")

#%% Meteorologic data
#Year,Month,Day,Hour,Minute,DHI,DNI,Dew Point,Surface Albedo,Wind Speed,Relative Humidity,Temperature,Pressure,Unnamed: 13,File

DF_met=pd.read_csv(data_path+"MeteorUnited.csv")
DF_met["Time Stamp"]=pd.to_datetime(DF_met["Year"].astype("str")+"-"+DF_met["Month"].astype("str")+"-"+DF_met["Day"].astype("str")+" "+DF_met["Hour"].astype("str")+":"+DF_met["Minute"].astype("str")+":00")
DF_met.drop(columns=["Unnamed: 0","Year","Month","Day","Hour","Minute","Unnamed: 13"],inplace=True)
print(DF_met.columns)

columns=DF_met.columns.tolist()

fig,(axes)=plt.subplots(3,3)
new_axes=axes.flatten()
plt.xticks(rotation=30)
for k in tqdm(range(len(columns[:-2]))):
    plt.xticks(rotation=30)
    sns.lineplot(data=DF_met,x="Time Stamp", y=columns[:-2][k],ax=new_axes[k],hue="File",legend=False)
    new_axes[k].set_ylabel(columns[k],size="x-small")
    new_axes[k].set_xlabel("Date",size="xx-small")
    plt.xticks(rotation=30)
new_axes[-1].set_axis_off()
handles, labels = new_axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc='lower right')
fig.set_size_inches(14, 7)
plt.suptitle("Stations in costa rica")
plt.savefig(path+"/Meteorology.png")
plt.tight_layout(pad=2.5)

print("First meteor plot done")




print("Total time: {} minutes".format((datetime.datetime.now().timestamp()-start)/60))