# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 09:02:06 2016

@author: aa
"""
import numpy as np
import matplotlib.pyplot as plt

def plotData(X,y):
    pos=np.where(y == 1)
    neg=np.where(y==0)
    
    plt.plot(X[pos,0],X[pos,1],'k+',linewidth=1,markeredgewidth=1)
    plt.plot(X[neg,0],X[neg,1],'yo',linewidth=1,markeredgewidth=1)
