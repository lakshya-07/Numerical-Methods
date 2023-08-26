# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 08:31:50 2021

@author: Lakshya Singh
"""

# lcr second order differential equation using rk4 

import matplotlib.pyplot as plt
import numpy as np


e = 0.1
l = 1
c = 0.25 
r = 4

if (r > 2*np.sqrt(l/c)):
    print("This circuit is overdamped")
elif(r == 2*np.sqrt(l/c)):
    print("This circuit is critically damped")
else:
    print("This circuit is underdamped")    
    
    
ti = 0.0
i = 0.0
q = 0.0
tf = 30.0 
h = 0.001 


#defining functions
def funct1(q,i,t):
    return i 

def funct2(q,i,t):
    return (e - i*r - q/c)/l

time = []
curr = []
charg = []

while ti <= tf:
    time.append(ti)
    charg.append(q)
    curr.append(i)
    k1 = h*funct1(q,i,ti)
    l1 = h*funct2(q,i,ti)
    
    k2 = h*funct1(q + k1/2,i +l1/2,ti + h/2)
    l2 = h*funct2(q + k1/2,i +l1/2,ti + h/2)
    
    k3 = h*funct1(q + k2/2,i +l2/2,ti + h/2)
    l3 = h*funct2(q + k2/2,i +l2/2,ti + h/2)
    
    k4 = h*funct1(q + k3,i +l3,ti + h)
    l4 = h*funct2(q + k3,i +l3,ti + h)
    
    q += (k1 + 2.0*k2 + 2.0*k3 + k4)/6.0
    i += (l1 + 2.0*l2 + 2.0*l3 + l4)/6.0
    ti = ti + h
    
print("Using Rk4 method, At t =",ti,", q =",q,",i =",i) 

plt.subplot(2,2,1)
plt.plot(time,curr)
plt.xlabel("time")
plt.ylabel("Current")
plt.suptitle("Damping of LCR circuit")
plt.tight_layout(w_pad = 5)

plt.subplot(2,2,2)
plt.plot(time,charg)
plt.xlabel("time")
plt.ylabel("Charge")

plt.subplot(2,2,3)
plt.plot(charg,curr)
plt.xlabel("Charge")
plt.ylabel("Current")










   
    
    
    
    
    
    