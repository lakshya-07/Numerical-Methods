# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 20:46:06 2021

@author: Lakshya Singh
"""

#integration with simpson and trapezoidal of exp(-x)

x = [0,1/2,1,3/2,2]
y = [1,0.6064,0.3676,0.2231,0.1353]

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