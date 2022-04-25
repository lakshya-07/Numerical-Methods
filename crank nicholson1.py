# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 19:36:20 2022

@author: Lakshya Singh
"""

# crank nicholson method for 1-D heat equation


import numpy as np
import matplotlib.pyplot as plt


#step sizes
h = 0.25 #step size for values of x
r = 1    #parameter
c = 1/16 #constant

k = (h*h*r)/c # step size for values of t


#arrays for step sizes
x = np.arange(0,1+h,h)
t = np.arange(0,1+k,k)

#entering initial and boundary conditions
intil = 0
bdry = [0,200*t]

n = len(x)
m = len(t)


U = np.zeros((m,n))

#feeding initial and boundary conditions to array U
U[0,:] = intil
U[:,0] = bdry[0]
U[:,-1] = bdry[-1]

print("The initial table for the values of u: ")
#Here the columns heads are values of x and rows are the step sizes for time
print(U)
print()


#generating matrix for unknown values
A = np.diag([2+2*r]*(n-2),0)
A += np.diag([-r]*(n-3),1)
A += np.diag([-r]*(n-3),-1)
print("The matrix generated for unknown values is A = ",A)

print()


#generating matrix for known values
B = np.zeros((n-2))

for j in range(m-1):
    for i in range(1,n-1):
        B[i-1] = (2-2*r)*U[j,i] + r*U[j,i+1] + r*U[j,i-1] + r*U[j+1,i+1] + r*U[j+1,i-1]

print("The matrix generated for known values is B = ",B)

print()


# solving matrix system of A and B
sol  = np.linalg.solve(A, B)
print("The solution of generated matrix system (A & B) is given by: ",sol)

for j in range(1,m):
    for i in range(1,n-1):
        U[j,i] = sol[i-1]

print()
print("The final table for the values of u: ")
print(U)


plt.plot(x,U[0,:])
plt.plot(x,U[1,:])
plt.title("Graph for given 1-D heat equation")
plt.xlabel("Values of x")
plt.ylabel("Values of y")
plt.legend(["At t = 0","At t = 1"])


    
    
