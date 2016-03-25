# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 09:28:03 2016

@author: aa
"""
import numpy as np

def linearKernel(X):
    x1=X[:,0].flatten()
    x2=X[:,0].flatten()
    res=np.dot(x1.transpose(),x2)
    return res