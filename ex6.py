# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 08:52:37 2016

@author: aa
"""

import scipy.io as sio
import PD
import ST
import GK
import matplotlib.pyplot as plt
import DP
#import VBL


data=sio.loadmat('ex6data1')
X=data['X']
y=data['y']

#Part One: Loading and Visualizing Data
print 'One:=======================Loading and Visualizing Data...'
PD.plotData(X,y)
plt.title('Example Dataset 1')
plt.axis(xmin=0,xmax=4.5,ymin=1.5,ymax=5)
plt.show()
print ''

#Part Two: Training Linear SVM
print 'Two:========================Training Linear SVM...'
C=1
model=ST.svmTrain(X,y,C,'linear',1e-3,20)
plt.title('Example Dataset 1')
plt.axis(xmin=0,xmax=4.5,ymin=1.5,ymax=5)
plt.show()

#Part Three: Implementing Gaussian Kernel
print 'Three: =======================Evaluating the Gaussian Kernel...'
x1=[1,2,1]
x2=[0,4, -1]
sigma=2
sim=GK.gaussianKernel(x1,x2,sigma)
print 'Gaussian Kernel between x1=[1;2;1], x2=[0;4;-1],sigma=2 : %6.4f \n (This value should be about 0.324652)' % sim

#Part Four: Visualizing Dataset 2
print 'Four: ==========================Visualizing Dataset2...'
data=sio.loadmat('ex6data2')
X=data['X']
y=data['y']
PD.plotData(X,y)
plt.title('Example Dataset 2')
plt.axis(xmin=0,xmax=1,ymin=0.4,ymax=1)
plt.show()

#Part Five: Training SVM with RBF Kernel
print 'Five: =============================Training SVM with RBF Kernel (Dataset 2)...'
C=10
model=ST.svmTrain(X,y,C,'rbf')
plt.title('Example Dataset 2')
plt.axis(xmin=0,xmax=1,ymin=0.4,ymax=1)
plt.show()

#Part Six: Visualizing Dataset3
print 'Six: ================Loading and Visualizing Dataset 3...'
data=sio.loadmat('ex6data3')
X=data['X']
y=data['y']
PD.plotData(X,y)
plt.title('Example Dataset 3')
plt.axis(xmin=-0.6,xmax=0.4,ymin=-0.8,ymax=0.6)
plt.show()

#Part Seven: Training SVM with RBF Kernel (Dataset 3)
print 'Seven: ==========Training SVM with RBF Kernel (Dataset 3)...'
Xval=data['Xval']
yval=data['yval']
res=DP.dataset3Params(X,y,Xval,yval)
C=res[0]
model=ST.svmTrain(X,y,C,'rbf')
plt.title('Example Dataset 3')
plt.axis(xmin=-0.6,xmax=0.4,ymin=-0.8,ymax=0.6)
plt.show()



















