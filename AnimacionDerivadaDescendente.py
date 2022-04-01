# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 12:17:42 2022

@author: johnf
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-10,100,0.1)
y=x**2-6*x
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.grid()

w=90
z=w**2-6*w
plt.plot(w,z,"o")
wp=np.inf
alfa=0.1
tol=0.001
while (np.abs(w-wp)>tol):
    wp=w
    w=w-alfa*(2*w-6)
    z=w**2-6*w    
    plt.plot(w,z,"ok")
    
    plt.pause(1)
    print(w)

