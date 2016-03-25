# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 09:22:59 2016

@author: aa
"""
from sklearn import svm
import matplotlib.pyplot as plt

def svmTrain(X,y,C,funcStr,tol=None,max_passes=None):
    if not tol:
        tol=1e-3
    if not max_passes:
        max_passes=5

    clf=svm.SVC(C,kernel=funcStr, gamma=0.001)
    clf.fit(X,y.ravel())
    
    
    #get the parameters
#    if funcStr=='linear':
#        xx=np.linspace(min(X[:,0]),max(X[:,0]),100)
#        w=clf.coef_[0]
#        a=-w[0]/w[1]
#        yy=a*xx-clf.intercept_[0]/w[1]      
#        plt.plot(xx,yy,'-b')
#        PD.plotData(X,y)
#    else:
#        print 'Gaussian Kernel'
#        x_min,x_max=X[:,0].min()-1,X[:,0].max()+1
#        y_min,y_max=X[:,1].min()-1,X[:,1].max()+1
#        xx,yy=np.meshgrid(np.arange(x_min,x_max,0.005),np.arange(y_min,y_max,0.005))
#        Z=clf.predict(np.c_[xx.ravel(),yy.ravel()])
#        Z=Z.reshape(xx.shape)
#        plt.contour(xx,yy,Z,levels=[0], linewidths=1, colors='blue' )
#        PD.plotData(X,y)
   #     plt.axis(xmin=-1,xmax=1,ymin=-1,ymax=1)   
    return clf

  
