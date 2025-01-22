# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 16:08:17 2021

@author: Lakshya Singh
"""
#interpolation of given data 

import numpy as np
import math as m
import matplotlib.pyplot as plt


def pval(p,n):
    t = p
    for i in range(1,n):
        t = t*(p-i)
    return t


x = [1,2,3]
ylist = [3,2,2]

plt.plot(x,ylist, lw = 2, marker = 'o')
plt.ylabel("Values of x")
plt.xlabel("Values of y")
plt.title("Graph of given data")


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





        