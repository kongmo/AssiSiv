import numpy as np

def processEmail(data):
    fid=fopen('vocab.txt')

    n=1899
    vocabList=np.zeros((n,1))
    for i in range(n):
        tmp=read(fid,1)
        vocabList[i]=read(fid,1)
    close(fid)
    return vocabList
    
