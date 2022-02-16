# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 15:55:01 2022

@author: Lakshya Singh
"""

#gauss hermite quad integration

from scipy.integrate import quad
from scipy.special import hermite,roots_hermite
import numpy as np
from math import factorial as f
import matplotlib.pyplot as plt

# original: (1/(np.sqrt(2*np.pi*sig*sig)))*np.exp(-(x-2)**2/(2*sig*sig))*(x+3)

#implementing function
def Dirac(x,sig): 
    return (np.sqrt(2)*sig*x + 5)/(np.sqrt(np.pi))
    #return 1/(np.sqrt(np.pi))



funct = lambda x: (1/(np.sqrt(2*np.pi*sig*sig)))*np.exp(-(x-2)**2/(2*sig*sig))*(x+3)

 
def H(n,x): #generating hermite polynomial by series summation
    h = 0
    if(n % 2 == 0):
        l = int(n/2)
    else:
        l = int((n-1)/2)
        
    for r in range(0,l+1):
        h += (((-1)**r)*f(n)*((2*x)**(n-2*r)))/((f(r)*f(n-2*r))) 
    return h   
 

a = -np.inf # float(input("Enter lower limit: "))
b = np.inf # float(input("Enter upper limit: "))

p = int(input("Enter the point of quadrature formula: "))

sig = float(input("Enter the value of sigma for dirac delta: "))

#calculating integral using inbuilt function
actval = quad(funct,a,b)
print("The value of integral using inbuilt function is =",actval)

   
sols = roots_hermite(p)

#taking roots from inbuilt
roots = np.roots(hermite(p))
roots.sort()
print("The inbuilt roots and weights are = ",sols)

#generating weights
w = [((2**(p-1))*f(p)*np.sqrt(np.pi))/(p*p*((H(p-1,r))**2)) for r in roots]

print()

#print("The roots are = ",roots)

print("The calculated weights are = ",w)


calval = 0
for j in range(0,len(roots)):
    #calval += sols[1][j]*Dirac(sols[0][j],sig) 
    calval += w[j]*Dirac(roots[j],sig) 

    

print("The calculated quadrature value of integral is = ",calval)


# using simpson method 
def simp(a,b,n):
    h = (b-a)/n
    s1 = funct(a)+ funct(b)
    
    for i in range(1,n):
        v = a + i*h
        
        if (i % 2 == 0):
            s1 = s1 + 2*funct(v)
        else:
            s1 = s1 + 4*funct(v)
        
    return print("The value of integral by simpson =",s1*(h/3))

simp(-1000,1000,100000)


#plotting the dirac delta funct

for sig in [1,0.1,0.01,0.5] :
    x = np.linspace(0,5,200)
    plt.plot(x,funct(x))
    plt.xlabel("Values of x")
    plt.ylabel("Values of y")
    plt.title("Plot for Dirac Delta Function")
    plt.legend(["$\sigma$ = 1.0","$\sigma$ = 0.1","$\sigma$ = 0.01","$\sigma$ = 0.5"])

    




