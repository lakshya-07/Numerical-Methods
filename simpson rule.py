# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 10:02:34 2021

@author: Lakshya Singh
"""


#integration with simpson and trapezoidal of exp(-x)
import numpy as np

def P(n,x): 
    if(n == 0):
        return 1 
    elif(n == 1):
        return x 
    else:
        return (((2*n)-1)*x*P(n-1,x)-(n-1)*P(n-2,x))/n
    
def funct(x):
    return (1/(np.sqrt(2*np.pi*sig*sig)))*np.exp(-(x-2)**2/(2*sig*sig))*(x+3)


def intgrt(a,b,n):
    h = (b-a)/n
    s1 = funct(a)+ funct(b)
    
    for i in range(1,n):
        v = a + i*h
        
        if (i % 2 == 0):
            s1 = s1 + 2*funct(v)
        else:
            s1 = s1 + 4*funct(v)
        
    return print("The value of integral =",s1*(h/3))
    

a = float(input("Enter the value of lower limit: "))
b = float(input("Enter the value of upper limit: "))
n = int(input("Enter the value of 'n' for step size: "))

sig = 0.1
intgrt(a,b,n)







    
    