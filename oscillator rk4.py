# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 08:31:50 2021

@author: Lakshya Singh
"""

# harmonic oscillator differential equation using rk4 

import matplotlib.pyplot as plt
import numpy as np

b = 2
k = 10
F = 1
w = 2
m = 1

   
ti = 0.0
x = 0.0
v = 2
tf = 20.0 
h = 0.1 


#defining functions
def funct1(x,v,t):
    return v 

def funct2(x,v,t):
    return (-b*v-k*x + F*np.cos(w*t))/m

time = []
dist = []
vel = []

while ti <= tf:
    time.append(ti)
    dist.append(x)
    vel.append(v)
    k1 = h*funct1(x,v,ti)
    l1 = h*funct2(x,v,ti)
    
    k2 = h*funct1(x + k1/2,v +l1/2,ti + h/2)
    l2 = h*funct2(x + k1/2,v +l1/2,ti + h/2)
    
    k3 = h*funct1(x + k2/2,v +l2/2,ti + h/2)
    l3 = h*funct2(x + k2/2,v +l2/2,ti + h/2)
    
    k4 = h*funct1(x + k3,v +l3,ti + h)
    l4 = h*funct2(x + k3,v +l3,ti + h)
    
    x = x + (k1 + 2.0*k2 + 2.0*k3 + k4)/6.0
    v = v + (l1 + 2.0*l2 + 2.0*l3 + l4)/6.0
    ti = ti + h
    
print("Using Rk4 method At t =",ti,", x =",x,",v =",v) 

plt.subplot(2,2,1)
plt.plot(time,dist)
plt.xlabel("time")
plt.ylabel("Displacement")
plt.suptitle("Damping of Harmonic Oscillator")
plt.tight_layout(w_pad = 6)

plt.subplot(2,2,2)
plt.plot(time,vel)
plt.xlabel("time")
plt.ylabel("Velocity")

plt.subplot(2,2,3)
plt.plot(dist,vel)
plt.xlabel("Displacement")
plt.ylabel("Velocity")










   
    
    
    
    
    
    