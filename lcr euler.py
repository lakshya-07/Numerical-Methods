# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 09:10:05 2021

@author: Lakshya Singh
"""

# lcr second order differential equation by euler method + odeint

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

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
h = 0.01 


#defining functions
def funct1(q,i,t):
    return i 

def funct2(q,i,t):
    return (e - i*r - q/c)/l

def du_dx(u,t):
    # here u[0] = q, u[1] = i 
    return [u[1],(e - u[1]*r - u[0]/c)/l]

uo = [q,i]
t_ode = np.linspace(0,30,500)
uf = odeint(du_dx,uo,t_ode)
q_ode = uf[:,0]
i_ode = uf[:,1]


print("Using inbuilt ode method at t =",t_ode[499],", q =",uf[499,0],",i =",uf[499,1]) 

time = []
curr = []
charg = []

while ti <= tf:
    time.append(ti)
    charg.append(q)
    curr.append(i)
    q = q + h*funct1(q,i,ti)
    i = i + h*funct2(q,i,ti)
    ti = ti + h
    
print("Using euler method at t =",ti,", q =",q,",i =",i) 

fig = plt.figure()
plt.subplot(2,2,1)
plt.plot(time,curr, ls = "dashed", lw = 2)
plt.plot(t_ode,i_ode)
plt.xlabel("time")
plt.ylabel("Current")
plt.suptitle("Damping of LCR circuit")
plt.tight_layout(w_pad = 5)
fig.legend(["Euler method","Inbuilt method"], loc = 'lower right')

plt.subplot(2,2,2)
plt.plot(time,charg, ls = "dashed", lw = 2)
plt.plot(t_ode,q_ode)
plt.xlabel("time")
plt.ylabel("Charge")

plt.subplot(2,2,3)
plt.plot(charg,curr, ls = "dashed", lw = 2)
plt.plot(q_ode,i_ode)
plt.xlabel("Charge")
plt.ylabel("Current")







   
    
    
    
    
    
    