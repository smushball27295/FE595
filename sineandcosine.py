# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 16:09:16 2020

@author: ramesh
"""

import numpy as np
import matplotlib.pyplot as plt   

def func(): 
    x = np.arange(0,2*np.pi,0.1)   
    y = np.sin(x)
    z = np.cos(x)
    plt.plot(x,y,x,z)
    plt.show()

if _name_=="_main_":
    func()






















