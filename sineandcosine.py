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
    x = np.arange(0,2*np.pi,0.1)   
    y = np.sin(x)
    z = np.cos(x)
    plt.plot(x,y,x,z)
    plt.show()
    
func()    

if _name_=="_main_":
    func()






















plt.plot(x,y,x,z)
plt.xlabel('x values from 0 to 4pi')  # string must be enclosed with quotes '  '
plt.ylabel('sin(x) and cos(x)')
plt.title('Plot of sin and cos from 0 to 4pi')
plt.legend(['sin(x)', 'cos(x)'])      # legend entries as seperate strings in a list
plt.show()