# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 15:55:01 2022

@author: Lakshya Singh
"""

#gauss laguerre quad integration


from scipy.special import laguerre
from scipy.special import roots_laguerre
import numpy as np
from math import factorial as f


def Lag(n,x): #generating laguerre polynomial by series summation
    l = 0
    for k in range(0,n+1):
        l += (f(n)*((-1)**k)*(x**k))/(f(n-k)*f(k)*f(k))
    return l

def L(n,x): #generating leguerre polynomial by recurrsion relation
    if(n == 0):
        return 1 
    elif(n == 1):
        return 1-x 
    else:
        return ((2*n-1-x)*L(n-1,x)-(n-1)*L(n-2,x))/n 
    
    

#implementing function
funct = lambda x : np.exp(x)/(x**2 + 2)


p = int(input("Enter the point of quadrature formula: "))


sols = roots_laguerre(p)

#taking inbuilt roots
roots = np.roots(laguerre(p))
roots.sort()
print("The roots and weights are = ",sols)

#calculating weights
w = [r/(((p+1)*L(p+1,r))**2) for r in roots]
print()
print("The calculated weights are = ",w)


calval = 0
for j in range(0,len(sols[0])):
    calval += w[j]*funct(roots[j]) 
    #calval += sols[1][j]*funct(sols[0][j]) 

print("The calculated value of integral is = ",calval)









