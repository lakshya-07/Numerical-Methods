# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 15:48:03 2021

@author: Lakshya Singh
"""
#euler sol for dy/dx = exp(-x) at x = 10

import numpy as np
import matplotlib.pyplot as plt


def funct(x,y): 
    return np.exp(-x)

xi = 0
xf = 10
h = 0.001
x = 0 
y = 0

n = int((xf-xi)/h)

x_plot = []
y_euler = []
y_anlyt = []

for i in range(1,n+1):
    y = y + funct(x,y)*h
    x = x + h
    x_plot.append(x)
    y_euler.append(y)
    y_anlyt.append(1-funct(x,y))

A = 1-funct(10,0)
print("The actual value of y at x = 10 is",A)
print("At x =",x,", y =",y)
print("The percentage error in the calculation is ",((np.abs(A-y))/A)*100,"%")

plt.plot(x_plot,y_euler, ls = "dotted", lw = 3.2)
plt.plot(x_plot,y_anlyt)
plt.legend(["Euler graph","Actual graph"])
plt.title(r"Plot for $ \frac{dy}{dx} = e^{-x}$")
plt.xlabel("Values of x")
plt.ylabel("Values of y") 
















    
    