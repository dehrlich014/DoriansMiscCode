"""This document builds the Newton and Secant methods and applies each
to the function (givein in Ascher & Greif) f(x) = 2*cosh(x/4) - x, which has a root.
Then, a graph is made that shows where Newton and Secant each come in approximating
the root ."""

import numpy as np
import matplotlib.pyplot as plt

atol = 10**(-8)

def NewtonsMethod(f,fprime,x0):
    x = [x0]
    x1 = x[0] - (f(x[0])/fprime(x[0]))
    x.append(x1)
    k = len(x)-1
    curr = abs(x[k] - x[k-1])
    #Initializing the sequence that is Newtons Method.
    
    #Newton's Method:
    #x_next = x_curr - (f(x_curr))/(fprime(x_curr)).
    
    while curr > atol:
        xnew = x[k] - (f(x[k])/fprime(x[k]))
        x.append(xnew)
        k = len(x)-1
        #Updating our index k for storing data in vector x.
        curr = abs(x[k] - x[k-1])
        #And retaking the difference between previous steps. We stop when two consectuive steps
        #are *very* close to each other i.e. within atol of each other.
    x = np.array(x)
    return x


def SecantMethod(f,x0,x1):
    x = [x0,x1]
    x2 = x[1] - ((f(x[1])*(x[1] - x[0]))/(f(x[1]) - f(x[0])))
    x.append(x2)
    k = len(x)-1
    curr = abs(x[k] - x[k-1])
    
    #Again, this is the initialization of the secant method.
    #We need to do the first step manually so that our while loop may run.
    
    #Secant method generates a series of approximating secant lines.
    #In particular, the secant method is:
    #x_next = x_curr - f(x_next)*1/((f(x_curr) - f(x_prev))/(x_curr - x_prev)).
    #The secant method uses the approx to the derivative where Newton uses the real thing.
    while curr > atol:
        xnew = x[k] - ((f(x[k])*(x[k] - x[k-1]))/(f(x[k]) - f(x[k-1])))
        x.append(xnew)
        k = len(x)-1
        curr = abs(x[k] - x[k-1])
    x = np.array(x)
    return x

#For this demonstration, we'll use the Ascher/Greif function as our f.
def f(x):
    return (2*np.cosh(x/4) - x)

#And we'll hardcode in our derivative since it's readily available to us.
def fprime(x):
    return (.5*np.sinh(x/4) - 1)

x0 = 2
x1 = 3
xNewton = NewtonsMethod(f,fprime,x0)
xSecant = SecantMethod(f,x0,x1)
ab = np.arange(1,4,.05)
z = np.zeros(len(ab))
zNewton = np.zeros(len(xNewton))
zSecant = np.zeros(len(xSecant))
print(xNewton)
print(xSecant)
#plot the line y = 0
plt.plot(ab,z,'r--')
#plot the graph of y = f(x)
plt.plot(ab,f(ab))
plt.plot(xNewton,zNewton,'bs')
plt.plot(xSecant,zSecant,'gd')
plt.show()
