# -*- coding: utf-8 -*-
"""
Script file to show a transmission line with towers and conductor cables.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt

#Usar referencias de 230 kV depois alterar para 500 kV

df = pd.read_csv("c1.csv")
df = df.drop(['TIME'],axis=1)
dfa = df.to_numpy()

dfa[:,3]= dfa[:,3]*1000

rmin = 6.83

y_min = dfa[:,2] + rmin

plt.plot(dfa[:,3],dfa[:,2],'b',dfa[:,3],y_min,'r')

#plt.plot(df.DIST,df.ALT,'r',df.DIST,df.ALTmin,'b')

#Posição da Torre
xt1=0
xt2=5000

#Altura da torre
H = 130 

i_t1 = np.where(dfa[:,3]>=xt1)[0][0]
i_t2 = np.where(dfa[:,3]>=xt2)[0][0]

yt1 = dfa[i_t1,1] + H
yt2 = dfa[i_t2,1] + H

T1 = np.array([[xt1,dfa[i_t1,1]],[xt1,yt1]])

T2 = np.array([[xt2,dfa[i_t2,1]],[xt2,yt2]])

plt.plot(T1[:,0],T1[:,1],'k')
plt.plot(T2[:,0],T2[:,1],'k')