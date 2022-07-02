# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 18:31:29 2022

@author: Lakshya Singh
"""

#solving y" - 2y = 0 where y(0)= 1.2 & y(1) = 0.9 using shooting method

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_bvp

#intial guesses
g1 = -1
g2 = -2

#tolerance limit
e = 0.001

#initial conditions
xi = 0
yi = 1.2
xf = 1
yf = 0.9
h = 0.25

p = []
x = []
y = []

#analytically solved solution of given equation
def funct(x):
    return 0.15716*np.exp(np.sqrt(2)*x) + 1.04283*np.exp(-np.sqrt(2)*x)

for z in [g1,g2]:
    
   
       
    #defining functions
    def funct1(x,y,z):
        return  z
    
    def funct2(x,y,z):
        #dz/dx
        return 2*y 
    
    x_i = xi
    y_i = yi
    x_f = xf
    y_f = yf
    k = 0
    val = []
    print("--------------Iteration for intial guess =",z,"----------------")
    print("{:<5}{:<20}{:<25}{:<25}".format("i","x","y","z = dy/dx"))
    print("--------------------------------------------------------------")
    
    #solving differential equations by euler method
    while x_i <= x_f:
        print("{:<5}{:<20}{:<25}{:<25}".format(k,x_i,y_i,z))
        y_n = y_i + h*funct1(x_i,y_i,z)
        val.append(y_i)
        z = z + h*funct2(x_i,y_i,z)
        y_i = y_n
        x_i = x_i + h
        k += 1
    p.append(val[-1])
    
    print() 
       

print()

x_i = xi
y_i = yi
x_f = xf
y_f = yf

# defining array for plotting graphs

sol = np.linspace(xi,xf,20)

#for final iteration
if((abs(p[0]-y_f) >= e) and (abs(p[1]-y_f) >= e)):
    
    #using secant method formula for desired result
    z = g1 + ((g2-g1)/(p[1]-p[0]))*(y_f-p[0])
    k = 0
    print("-------Final Iteration for z = ",z,"---------")
    print("{:<5}{:<20}{:<25}{:<25}".format("i","x","y","z = dy/dx"))
    print("-------------------------------------------------------------")
    
    while x_i <= x_f:
        print("{:<5}{:<20}{:<25}{:<25}".format(k,x_i,y_i,z))
        y.append(y_i)
        x.append(x_i)
        y_n = y_i + h*funct1(x_i,y_i,z)
        z = z + h*funct2(x_i,y_i,z)
        y_i = y_n
        x_i = x_i + h
        k += 1

#plotting graph for actual functions & calculated points
plt.plot(x,y, marker ='o')
plt.plot(sol,funct(sol))
plt.title("Graph for y'' = 2y")
plt.xlabel("Values of x")
plt.ylabel("Values of y")
plt.legend(["Calculated points","Actual Function"])




        

    



     
  
        
    
    








