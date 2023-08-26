# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 14:37:21 2021

@author: Lakshya Singh
"""
#euler sol for radioactive decay

import numpy as np
import matplotlib.pyplot as plt


No = 8000
t_half = 3
k = np.log(2)/t_half

#analytical
A = No*np.exp(-k*9)

#euler method
t = 0
tf = 9
h = 1e-5
n = int((tf-t)/h)

t_plot = []
N_euler = []
N_anlyt = []


for i in range(1,n+1):
    No = No - h*No*k
    t = t + h
    t_plot.append(t)
    N_euler.append(No)
    N_anlyt.append(No*np.exp(-k*t))
    
print("The value of decay constant k is",k)

print("The actual number of atoms after 9 sec are",A) 
print("At t =",t,", N =",No)  
print("The percentage error in the calculated value is =",((A-No)/A)*100,'%')

#plots
plt.plot(t_plot,N_euler, ls = "dotted", lw = 3.2)
plt.plot(t_plot,N_anlyt)
plt.legend(["Euler graph","Actual graph"])
plt.title("Plot of Radioactive decay \n $N = N_{\circ} e^{-kt}$ Vs t")
plt.xlabel("Time(t) (seconds)")
plt.ylabel("Number of particles (N)") 


