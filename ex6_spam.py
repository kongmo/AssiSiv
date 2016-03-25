import PE
import EF
import scipy.io as sio
import STSpam
import numpy as np

#Part One: Email Preprocessing
print 'One: =============Email Preprocessing ...'
fileContent=open('emailSample1.txt','r').read()
wordIndices=PE.processEmail(fileContent)
print wordIndices
print ' '

#Part Two: Feature Extration
print 'Two:==================Extracting features from sample email (emailSample1.txt)...'

features=EF.emailFeatures(wordIndices)
print 'Length of features vector: ',len(features)
print 'Number of non-zero entries: ',sum(features>0)

#Part Three: Train Linear SVM for Spam Classification
print 'Three: ===============Train Linear SVM for Spam Classification...'
data=sio.loadmat('spamTrain') 
X=data['X']
y=data['y']
C=0.1
model=STSpam.svmTrain(X,y,C,'linear')
p=model.predict(X)
print 'Training Accuracy: %6.3f%%' % (np.mean(p == y.flatten())*100)

print ''
#Part Four: Test Spam Classsification
print 'Four: =================Test Spam Classification...'
data=sio.loadmat('spamTest')
Xtest=data['Xtest']
ytest=data['ytest']
p=model.predict(Xtest)
print 'Test Accuracy: %6.3f%%' % (np.mean(p == ytest.flatten())*100)


#Part Five: Top Predictions of Spam
print 'Five: ============Tope Prediction Spam...'
values=model.coef_[0]
m=values.size
keys=np.array(range(m))
pairs=np.array(zip(keys,values),dtype=[('x',int),('y',float)])
pairs.sort(order='y')
pairs=pairs[::-1]
fid=open('vocab.txt','r')
con=fid.readlines()
vocabList=[]
for line in con:
    txt=line[:-1].split('\t')[1]
    vocabList.append(txt)
fid.close()
for i in range(15):
    print '%8s    %6.4f' % (vocabList[pairs[i][0]],pairs[i][1])








