# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 21:15:21 2021

@author: Lakshya Singh
"""

#integration with simpson and trapezoidal of given data

import matplotlib.pyplot as plt


x = [0,2,4,6,8,10,12,14,16,18,20]
y = [0,10,18,25,29,32,20,11,5,2,0]

plt.plot(x,y, lw = 2, marker = 'o')
plt.ylabel("Velocity (km/min)")
plt.xlabel("time (min)")
plt.title("Velocity Vs Time Graph")

def simp():
    n = len(x)-1
    h = (x[-1]-x[0])/n
    
    s1 = y[0] + y[-1]
    for i in range(1,n):
        
        if (i % 2 == 0):
            s1 = s1 + 2*y[i]
        else:
            s1 = s1 + 4*y[i]
        
    return print("The value of integral by simpson's rule =",s1*(h/3))

simp()

def trap():
    n = len(x)-1
    h = (x[-1]-x[0])/n
    
    s1 = (y[0] + y[-1])*(h/2)
    s2 = 0
    for i in range(1,n):
        s2 = s2 + y[i]
        
    return print("The value of integral by trapezoidal rule =",s1+s2*h)

trap()    