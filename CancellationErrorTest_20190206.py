"""This file computes two versions of the same function, namely
sqrt(x+1) - sqrt(x) VS. 1/(sqrt(x) + sqrt(x+1)), and shows how
the relative error between these two expressions grows steadily as x grows logarithmically."""

import numpy as np
import matplotlib.pyplot as plt

def testCancelErr():
    fx1 = []
    fx2 = []
    t = []
    absErr = []
    relErr = []
    #These lists will contain the data we need as a function of t.
    #They will then be converted to arrays.
    for i in range(20):
        x = 10**i
        #Range 200 by 10 now.
        curr1 = np.sqrt(x+1) - np.sqrt(x)
        curr2 = 1/(np.sqrt(x+1) + np.sqrt(x))
        #curr will store each current iteration of each function and then get stored in
        #its respective arrays.
        fx1.append(curr1)
        fx2.append(curr2)
        t.append(x)
        #Here's where t gets built--it takes the values of x we used to eval fx1 and fx2.
        absErr.append(abs(curr1 - curr2))
        relErr.append(absErr[i]/abs(curr2))
    fx1 = np.array(fx1)
    fx2 = np.array(fx2)
    #Converting our lists to arrays now that they have been completely filled.
    t = np.array(t)
    absErr = np.array(absErr)
    relErr = np.array(relErr)
    print(fx1)
    print(fx2)
    plt.xscale('log')
    plt.yscale('log')
    plt.plot(t,fx1,'g',t,fx2,'b+',t,absErr,'r--',t,relErr,'y--')
    plt.show()
    #Notice how both absErr and relErr grow in a logarithmic scale. This is the accumulations of roundoff errors.
    for i in range(20):
        print(i,"|",t[i],"|",fx1[i],"|",fx2[i],"|",absErr[i],"|",relErr[i])
testCancelErr()
        
