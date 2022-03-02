# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 20:53:23 2022

@author: Lakshya Singh
"""

import numpy as np
import matplotlib.pyplot as plt

def p(x):
    return 0

def q(x):
    return -(1-(x/5))

def r(x):
    return x

xi = 1
xf = 3
h = 0.5

n = int((xf-xi)/h)  
print(n)

A = np.zeros((n-1,n-1))
B = np.zeros((n-1))


for i in range(1,n-1):
    A[i][i-1] = (2 - p(xi))/(2*h*h)
    xi = xi + h

xi = 1    
for i in range(n-1):
    A[i][i] = (-4 + 2*h*h*q(xi))/(2*h*h)  
    xi = xi + h

xi = 1
for i in range(n-2):
    A[i][i+1] = (2+p(xi))/(2*h*h)
    xi = xi + h
    
xi = 1
for i in range(n-1):
    xi = xi + h
    B[i] = r(xi)
    
     
print("A = ",A)
print("B = ",B)

x  = np.linalg.solve(A, B)
print("The solution of generated matrix is given by: ",x)


















    
    
