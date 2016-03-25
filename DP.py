# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 16:41:48 2016

@author: aa
"""
import numpy as np
from sklearn import svm

def dataset3Params(X,y,Xval,yval):
    tmpArray=[0.01,0.03,0.1,0.3,1,3,10,30]
    tmp=np.zeros(64)
    i=0
    
    x_min,x_max=Xval[:,0].min()-1,Xval[:,0].max()+1
    y_min,y_max=Xval[:,1].min()-1,Xval[:,1].max()+1
    xx,yy=np.meshgrid(np.arange(x_min,x_max,0.005),np.arange(y_min,y_max,0.005))    
    
    for c in tmpArray:
        for sig in tmpArray:
            clf=svm.SVC(c,kernel='rbf',gamma=sig) 
            clf.fit(X,y.ravel())
            predict=clf.predict(Xval)
            tmp[i]=np.mean(predict.flatten() != yval.flatten())
            i=i+1
    pos=tmp.argmin()
    if pos == 0:
        C=tmpArray[0]
        sigma=tmpArray[0]
    else:
        C=tmpArray[int((pos+1)/8)-1]
        sigma=tmpArray[np.mod(pos+1,8)]
    return C,sigma