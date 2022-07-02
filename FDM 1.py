# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 20:53:23 2022

@author: Lakshya Singh
"""
#finite differnce method for differential equations
#solving y" - y = 0 where y(0)= 0 & y(2) = 3.62686 

import numpy as np
import matplotlib.pyplot as plt

def p(x):
    return 0

def q(x):
    return -1

def r(x):
    return 0

#initial boundary conditions
xi = 0
xf = 2
yi = 0
yf = 3.62686

#step size
h = 0.5

n = int((xf-xi)/h)  

x = np.arange(xi,xf+h,h)

y = []


#defining arrays  

B = np.zeros((n-1))



#formations of tridiagonal matrix


A = np.diag([(-4 + 2*h*h*q(x[1:-2]))/(2*h*h)]*(n-1),0)

A += np.diag([(2 - h*p(x[1:-2]))/(2*h*h)]*(n-2),1)

A += np.diag([(2 + h*p(x[1:-2]))/(2*h*h)]*(n-2),-1)




B[0] = r(x[1])-yi*(2 + h*p(x[1]))/(2*h*h)
B[1:] = r(x[2:len(B)])
B[-1] = r(x[-2])-yf*(2 - h*p(x[-2]))/(2*h*h)

  

    
#solution of generated matrices    
print("Triadiagonal matrix, A = ",A)
print("matrix B = ",B)

sol  = np.linalg.solve(A, B)
print("The solution of generated matrix system (A & B) is given by: ",sol)


y = [sol[i] for i in range(len(sol))]
y.append(yf)
y.insert(yi,0)

plt.plot(x,y)





"""
import numpy as np
import matplotlib.pyplot as plt

def p(x):
    return 0

def q(x):
    return -1

def r(x):
    return x*(x-4)

#initial boundary conditions
xi = 0
xf = 4
yi = 0
yf = 0

#step size
h = 1

n = int((xf-xi)/h)  


#defining arrays  
val = np.zeros((n-1))
A = np.zeros((n-1,n-1))
B = np.zeros((n-1))

val[0] = yi
val[-1] = yf


#formations of tridiagonal matrix
s = xi
for i in range(1,n-1):
    A[i][i-1] = (2 - h*p(s))/(2*h*h)
    s = s + h

l = xi
for i in range(n-1):
    A[i][i] = (-4 + 2*h*h*q(l))/(2*h*h)  
    l = l + h

m = xi
for i in range(n-2):
    A[i][i+1] = (2 + h*p(m))/(2*h*h)
    m = m + h
    
k = xi
for i in range(n-1):
    k = k + h
    B[i] = r(k)-val[i]*(2 - h*p(k))/(2*h*h)
    
    
#solution of generated matrices    
print("A = ",A)
print("B = ",B)

sol  = np.linalg.solve(A, B)
print("The solution of generated matrix system is given by: ",sol)


"""
















    
    
