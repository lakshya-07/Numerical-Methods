# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 20:31:55 2021

@author: Lakshya Singh
"""

#interpolation for sin(x)

import numpy as np
import math as m
import matplotlib.pyplot as plt

def pval(p,n):
    t = p
    for i in range(1,n):
        t = t*(p-i)
    return t


x = [10,20,30,40,50,60,70,80,90]
ylist = [0.1736,0.3420,0.5,0.6427,0.7660,0.8660,0.9396,0.9848,1]

plt.plot(x,ylist, lw = 2, marker = 'o')
plt.ylabel("Values of x")
plt.xlabel("Values of y")
plt.title("Graph of sin(x)")

n = len(x)
val = float(input("Enter the value of point you want to find: "))

a = np.interp(val,x,ylist)
print("The value of y at x = ",val,"using inbuilt function is",a)
        
y = np.zeros((n,n))

for k in range(0,n):
    y[k][0] = ylist[k]

        
for i in range(1,n):
    for j in range(0,n-i):
        y[j][i] = y[j+1][i-1] - y[j][i-1]


p = (val - x[0])/(x[1] - x[0])

s = y[0][0]

for i in range(1,n):
    s = s + (pval(p,i)*y[0][i])/m.factorial(i)
    
print("The calculated value of y at x = ",val,"is",s)    





        