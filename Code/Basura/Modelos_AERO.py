#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Model of energy production of eolic generators
Based on script in matlab aero.m by David Rosero DDS.SAS
""" 

import numpy as np
import matplotlib.pylab as plt
import datetime
import pathlib
from scipy.optimize import curve_fit
path=str(pathlib.Path(__file__).parent.absolute())
#External parameters depending on region or machine
Air_density=1.225 #densidad del aire (kg/m^3)
r=5 #Longitud de las aspas (m)
beta=0  #Angulo de ataque
RPM=16  #Velocidad rotacional de aereogenerador
ohm=r*RPM*0.10472

Vels=np.arange(1,20.0,0.1)
# Velocity=np.genfromtxt("") #Activate with values of air velocity taken from meteorological stations
Velocity=np.array([7,8,7,6,5,7,8,6,5,8,7,5,3,3,3,4,5,6,7,8,9,9,5,8,7,4,5,6,3,2,5,4,4,6,9,5,8,7,3,10,12,5,4,6,9,5,3,4,3,6,7,7,8,4,3]) #Example velocities to test code
y, bins= np.histogram(Velocity,density=False) #Distribution of velocities
x=np.array([(bins[i]+bins[i+1])/2 for i in range(len(bins)-1)]) # midpoint value of velocities bins

def Weibull(x,lamb,k): 
    """Weibull function as found in literature with parameters lambda and k

    Args:
        x (float or np.array): input data generated from distribution or np.histogram
        lamb (Float): Lambda parameter from Weibull function
        k (Float): K parameter from Weibull function

    Returns:
        float or np.array: Expected value from weibull distribution for a value x with parameters lamb and k
    """    
    f=(k/lamb)*((x/lamb)**(k-1))*(np.exp((x/lamb)**k))
    return f

params,cov=curve_fit(Weibull,x,y)
W_lamb=params[0]
W_k=params[1]

FVel=Weibull(Vels,W_lamb,W_k)

L=ohm*r/np.array(Vels)
InvDelta=(1/L)-0.035
CP=0.5*((116*InvDelta)-5)*np.exp(-21*InvDelta)
P=(1/2)*Air_density*CP*np.pi*(r**2)*(Vels**3.0)
E=P*FVel
plt.style.use('ggplot')
plt.plot(FVel,E)
plt.xlabel("Velocidad del viento (m/s)")
plt.ylabel("Energia (Wh)")
plt.show()












    