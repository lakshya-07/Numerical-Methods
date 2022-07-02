# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 14:25:38 2022

@author: Lakshya Singh
"""

# fourier series for a square wave:
    
import numpy as np
from scipy.signal import square
import matplotlib.pyplot as plt


trm = 50 #terms of the series

l = np.pi

#function for square wave
def funct(x):  
    if((x > -l) and (x < 0)):
        return -1
    else:
        return 1

#function for fourier constants
ao = lambda x : (1/l)*funct(x)
an = lambda x : (1/l)*funct(x)*np.cos((n*x*np.pi)/l)
bn = lambda x : (1/l)*funct(x)*np.sin((n*x*np.pi)/l)


#function for integration by simpson 1/3 rule

def simp(funct,a,b,n):
    h = (b-a)/n
    s1 = funct(a)+ funct(b)
    
    for i in range(1,n):
        v = a + i*h
        
        if (i % 2 == 0):
            s1 = s1 + 2*funct(v)
        else:
            s1 = s1 + 4*funct(v)
        
    return s1*(h/3)

#defining limits
a = -l
b = l

# n for simpson step size
p = 1000


An = []
for n in range(trm):
    An.append(simp(an,a,b,p))

Bn = []    
for n in range(trm):
    Bn.append(simp(bn,a,b,p))    
    
 
print("The calculated values of ao = ",simp(ao,a,b,p))
print()
print("The calculated values of an = ",An)
print()
print("The calculated values of bn = ",Bn)

#function for fourier series
def nfunct(v):
    s = simp(ao,a,b,p)/2
    for i in range(trm):
        s += An[i]*np.cos((i*v*np.pi)/l) +  Bn[i]*np.sin((i*v*np.pi)/l)
    return s

#plotting the graph for square wave using inbuilt function and generated fourier series

x = np.arange(-l,l,0.001)
y = square(x)
plt.plot(x,nfunct(x))
plt.plot(x,y,lw = 3,ls ="dotted",color = "red")
plt.grid(True, which='both')
plt.xlabel("Values of x")
plt.ylabel("Values of f(x)")
plt.title("Graph for Fourier series of Square Wave")


    















