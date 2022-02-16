# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 18:15:17 2022

@author: Lakshya Singh
"""

#gauss legendre quad integration
#includes functions of problem 1 and problem 2 of assignment 1


from scipy import integrate
from scipy.special import legendre 
from scipy.special import roots_legendre
import numpy as np
from math import factorial as fact
from scipy import misc


def P(n,x): #generating legendre polynomial by recurrsion relation
    if(n == 0):
        return 1 
    elif(n == 1):
        return x 
    else:
        return (((2*n)-1)*x*P(n-1,x)-(n-1)*P(n-2,x))/n

def L(n,x): #generating legendre polynomial by rodrigues formula
    p = 0
    for m in range(0,int(n/2)+1):
        p += (((-1)**m)*(fact(2*n-2*m))*(x**(n-2*m)))/((2**n)*(fact(m))*(fact(n-m))*(fact(n-2*m)))
    return p
    


funct = lambda x : P(2,x)*P(2,x)

#funct = lambda x : np.exp(-x**2)

#funct = lambda x : L(1,x)*L(2,x)


a = float(input("Enter lower limit: "))
b = float(input("Enter upper limit: "))

p = int(input("Enter the point of legendre quadrature formula: "))

actval = integrate.quadrature(funct,a,b)
print("The value of integral using inbuilt function is =",actval)


sols = roots_legendre(p)
print("The roots and weights are = ",sols)

#w = [2/((1-(r)**2)*(misc.derivative(legendre(p),r))**2) for r in sols[0]]
#print("The calculated weights are = ",w)


calval = 0
for j in range(0,len(sols[0])):
    calval += ((b-a)/2)*sols[1][j]*funct(((b-a)/2)*sols[0][j] + (b+a)/2) 

print("The calculated value of integral is = ",calval)







