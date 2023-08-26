# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 18:42:22 2021

@author: Lakshya Singh
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

def du_dx(u,t):
    e = 0.1 
    l = 1
    c = 0.25 
    r = 4
    # here u[0] = q, u[1] = i 
    return [u[1],(e - u[1]*r - u[0]/c)/l]

uo = [0,0]
t_ode = np.linspace(0,30,500)
uf = odeint(du_dx,uo,t_ode)
q_ode = uf[:,0]
i_ode = uf[:,1]

print(t_ode[499],uf[499,0],uf[499,1])

plt.subplot(2,2,1)
plt.plot(t_ode,i_ode)
plt.xlabel("time")
plt.ylabel("Current")
plt.suptitle("Damping of LCR circuit")
plt.tight_layout(w_pad = 5)

plt.subplot(2,2,2)
plt.plot(t_ode,q_ode)
plt.xlabel("time")
plt.ylabel("Charge")

plt.subplot(2,2,3)
plt.plot(q_ode,i_ode)
plt.xlabel("Charge")
plt.ylabel("Current")

