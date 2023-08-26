# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 09:31:10 2021

@author: Lakshya Singh
"""
#euler sol for newton's law of cooling

import numpy as np
import matplotlib.pyplot as plt

def funct(T):
    k = -0.8
    T_surr = 30     #in degrees
    return k*(T-T_surr)

ti = t = 0
T = 100
tf = 15
h = 0.001
n = int((tf - ti)/h)

A = 60*np.exp(-0.8*15) + 30
print("The actual temperature after 15 sec is",A)

t_plot = []
T_euler = []
T_anlyt = []


for i in range(1,n+1):
    T = T + funct(T)*h
    t = t + h
    t_plot.append(t)
    T_euler.append(T)
    T_anlyt.append(60*np.exp(-0.8*t) + 30)
    
print("At t = ",t,", T",T)  
print("The percentage error in the calculation is ",((np.abs(A-T))/A)*100,"%") 

  
plt.plot(t_plot,T_euler, ls = "dotted", lw = 3.2)
plt.plot(t_plot,T_anlyt)
plt.title(r"Plot of Newton's law of cooling:$\ \frac{dT}{dt} = k(T-T_s)$")
plt.xlabel("Time(t) (seconds)")
plt.ylabel("Temperature (T)") 
plt.legend(["Euler graph","Actual graph"])





    

    


