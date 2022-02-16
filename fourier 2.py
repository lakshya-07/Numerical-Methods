# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 15:32:11 2022

@author: Lakshya Singh
"""



from scipy.special import roots_legendre,legendre 
import numpy as np
from scipy.signal import square,sawtooth
from scipy.integrate import quad
import matplotlib.pyplot as plt


trm = 50

l = 3


#funct = lambda x : x+(x*x)

def funct(x):
    k = 3
    if(0 < x < (l/2)):
        return (2*k*x)/l
    else:
        return (2*k*(l-x))/l


ao = lambda x : (1/l)*funct(x)
an = lambda x : (1/l)*funct(x)*np.cos((n*x*np.pi)/l)
bn = lambda x : (1/l)*funct(x)*np.sin((n*x*np.pi)/l)


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


a = 0
b = l
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


def nfunct(v):
    s = simp(ao,a,b,p)/2
    for i in range(trm):
        s += An[i]*np.cos((i*v*np.pi)/l) +  Bn[i]*np.sin((i*v*np.pi)/l)
    return s


x = np.arange(-l,l,0.001)
y = square(x)
plt.plot(x,nfunct(x))
#plt.plot(x,funct(x),lw = 3,ls ="dotted",color = "red")
plt.grid(True, which='both')
plt.xlabel("Values of x")
plt.xlabel("Values of f(x)")
plt.title("Graph for Fourier series of f(x)")


    


act1 = quad(ao,a,b)
print("The values using inbuilt function are- ao = ",act1)




"""
def Gaussleg(funct,a,b,p):
    sols = roots_legendre(p)
    calval = 0
    for j in range(0,len(sols[0])):
        calval += ((b-a)/2)*sols[1][j]*funct(((b-a)/2)*sols[0][j] + (b+a)/2) 
    print("The calculated value of integral is = ",calval)
    
#Gaussleg(an,a,b,p)
#Gaussleg(bn,a,b,p)

def funct(x):
    if((x > -l) and (x < 0)):
        return -1
    else:
        return 1

"""











