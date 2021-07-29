#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Calcula la corriente dado el voltaje, iluminacion y la temperatura

Datos del arreglo solar MSX-60
Ia = solar (Va,G,T) = vector de voltaje
Ia,Va = vector de corriente y voltaje
G = numero de Suns (1 Sun = 1000 W/mˆ2)
T = Temp en grados Celcius

""" 
import numpy as np
import matplotlib.pylab as plt
import datetime
import pandas as pd
import pathlib
path=str(pathlib.Path(__file__).parent.absolute())
ts1=datetime.datetime.now().timestamp()
# Ia=solar(Va,Suns,TaC)
k = 1.38*10**-23    # # Constante de Boltzman’s
q = 1.60e-19        # # Carga de un electron
n=1.2               #Factor calidad de diodo
Vg=1.12             #Diodo band-gap
Ns=36               #Diodos en serie
T1=273+25           #Temperatura
Voc_T1 = 21.06/Ns   #Voltaje de circuito abierto a T1
Isc_T1 = 3.80       #Corriente de corto circuito
T2 = 273 + 75       #
Voc_T2 = 17.05 /Ns  # Voltaje de circuito abierto por celda a temperatura T2
Isc_T2 = 3.92       # Corriente de cortocircuito de la celda a temperatura T2
Suns=1000
TaC=25
TaK = 273 + TaC     # Temperatura de trabajo del arreglo
K0 = (Isc_T2 - Isc_T1)/(T2 - T1)     # Ecuacion (4)
IL_T1 = Isc_T1 * Suns                # Ecuacion (3) 1000W/m^2=Sun
IL = IL_T1 + K0*(TaK - T1)           # Ecuacion (2)
I0_T1=Isc_T1/(np.exp(q*Voc_T1/(n*k*T1))-1) # Ecuación (6)
I0= I0_T1*(TaK/T1)**(3/n)*np.exp(-q*Vg/(n*k)*((1./TaK)-(1/T1)))     #  Ecuación (5)
Xv = I0_T1*q/(n*k*T1) * np.exp(q*Voc_T1/(n*k*T1))                   #   Ecuacion (8)
dVdI_Voc = - 1.15/Ns / 2                       # dV/dI a Voc por celda desde la gráfica del fabricante
                        
Rs = - dVdI_Voc - 1/Xv                          # Ecuacion (7)# Rs resistencia serie por celda
A=1.5                                           # Calidad del diodo
Vt_Ta = A * k * TaK / q# # = A * kT/q


Vc = Va/Ns#





