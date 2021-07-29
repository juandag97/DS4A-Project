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

