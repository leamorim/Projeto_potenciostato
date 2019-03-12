# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 22:26:02 2019

Neste script testamos o uso do filtro de suavização Savitzky-Golav, suavização por média
e o uso da função find_peaks para encontro do pico da curva

@author: lucas
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter, medfilt,find_peaks

c = pd.read_csv("x10.csv")

x = c.iloc[:,-2].values
y = c.iloc[:,-1].values
y_n = c.iloc[:,-1].values

#Suavização Savtizky Golav
y_n = savgol_filter(y,window_length = 11,polyorder = 2)
y_n = medfilt(y,kernel_size = 9)#Filtro que utiliza a média
ret_y, dic = find_peaks(y,height = 1) #Encontrando o pico de ambas as curvas
ret_y_n, dic = find_peaks(y_n,height = 1)


y = c.iloc[:,-1].values
plt.clf()  
plt.xlabel("Potencial em Volts (V)")
plt.ylabel("Corrente em Microampere (µA)")
plt.plot(x,y, color = 'blue',label = 'Original')
plt.plot(x,y_n, color = 'red', label = 'Savitzky-Golav')
plt.scatter(x[ret_y],y[ret_y], c = 'blue')
plt.scatter(x[ret_y_n],y_n[ret_y_n], c = 'red')
plt.legend(loc='upper left')
plt.grid(True)
plt.show() 