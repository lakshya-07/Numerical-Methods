# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 19:22:04 2021

@author: Lakshya Singh
"""
# harmonic oscillator euler method + odeint

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


b = 2
k = 10
F = 1
w = 2
m = 1

   
ti = 0.0
x = 0.0
v = 2
tf = 20.0 
h = 0.001 


#defining functions
def funct1(x,v,t):
    return v 

def funct2(x,v,t):
    return (-b*v-k*x + F*np.cos(w*t))/m

def du_dx(u,t): #for odeint
    # here u[0]=x,u[1]=v
    return [u[1],(-b*u[1]-k*u[0] + F*np.cos(w*t))/m]

uo = [x,v]
t_ode = np.linspace(0,20,200)
uf = odeint(du_dx,uo,t_ode)
x_ode = uf[:,0]
v_ode = uf[:,1]

print("Using inbuilt ode function at t =",t_ode[199],", x =",uf[199,0],",v =",uf[199,1]) 
print()

time = []
dist = []
vel = []

while ti <= tf:
    time.append(ti)
    dist.append(x)
    vel.append(v)
    x = x + h*funct1(x,v,ti)
    v = v + h*funct2(x,v,ti)
    ti = ti + h
    
print("Using euler method at t =",ti,", x =",x,",v =",v) 

fig = plt.figure()
plt.subplot(2,2,1)
plt.plot(time,dist, ls = "dashed", lw = 2)
plt.plot(t_ode,x_ode)
plt.xlabel("time")
plt.ylabel("Displacement")
plt.suptitle("Damping of Harmonic Oscillator")
plt.tight_layout(w_pad = 6)
fig.legend(["Euler method","Inbuilt method"], loc = 'lower right')

plt.subplot(2,2,2)
plt.plot(time,vel, ls = "dashed", lw = 2)
plt.plot(t_ode,v_ode)
plt.xlabel("time")
plt.ylabel("Velocity")

plt.subplot(2,2,3)
plt.plot(dist,vel, ls = "dashed", lw = 2)
plt.plot(x_ode,v_ode)
plt.xlabel("Displacement")
plt.ylabel("Velocity")










   
    
    
    
    
    
    
