# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 11:32:43 2019

Este script utiliza a técnica de baseline "Asymmetric Least Squares Smoothing" by P. Eilers and H. Boelens in 2005
disponível no google schoolar.


@author: lucas
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import sparse
from scipy.sparse.linalg import spsolve

#There are two parameters: p for asymmetry and λ for smoothness
def baseline_alps(y, lam, p, niter=10):
  L = len(y)
  D = sparse.diags([1,-2,1],[0,-1,-2], shape=(L,L-2))
  w = np.ones(L)
  for i in range(niter):
    W = sparse.spdiags(w, 0, L, L)
    Z = W + lam * D.dot(D.transpose())
    z = spsolve(Z, w*y)
    w = p * (y > z) + (1-p) * (y < z)
  return z

csv = pd.read_csv("w6.csv")
x = csv.iloc[:,-2].values
y = csv.iloc[:,-1].values

b = np.array([])#Y

y1 = 0

for i in range (0,y.size):
    b = np.concatenate((b,np.array(y[i]+y1)),axis = None)
    y1 += 0.05

baseline = baseline_alps(b,lam = 3000,p = 0.0001)
sub = np.array([])

for i in range(0,len(b)):
    sub = np.concatenate((sub,np.array(b[i]-baseline[i])),axis = None)

y = csv.iloc[:,-1].values

plt.plot(x,b, color = 'blue',label = 'Curva Y')
plt.plot(x,baseline, color = 'green',label = 'Curva Baseline')
plt.plot(x,sub,color='red',label='Baseline Subtraído')
plt.plot(x,y,color='black',label='Curva Original')
plt.legend(loc='upper left')
plt.show()