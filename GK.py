# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 11:27:33 2016

@author: aa
"""
import numpy as np

def gaussianKernel(x1,x2,sigma):
    x1=np.array(x1).flatten()
    x2=np.array(x2).flatten()
    res=np.exp(((-(x1-x2)**2).sum())/(2.0*(sigma**2)))
    return res
    