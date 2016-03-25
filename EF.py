import numpy as np

def emailFeatures(wordIndices):
    n= 1899
    res=np.zeros(n)
    res[wordIndices]=1
    return res
