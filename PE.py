import re
import PS
import numpy as np

def processEmail(data):
 #   print '============Get Reference List============='    
    fid=open('vocab.txt','r')
#Get vacab content
    con=fid.readlines()
    vocabList=[]
    for line in con:
        txt=line[:-1].split('\t')[1]
        vocabList.append(txt)
    fid.close()
    vlist=dict(zip(vocabList,np.array(range(len(vocabList)))+1))

#    print '========content preprocessing=========='
    emailContent=data.lower()
    emailContent=re.sub('<[^<>]+>',' ',emailContent)
    emailContent=re.sub('[0-9]+','number',emailContent)
    emailContent=re.sub('(http|https)://[^\s]*', 'httpaddr',emailContent)
    emailContent=re.sub('[^\s]+@[^\s]+', 'emailaddr',emailContent)
    emailContent=re.sub('[$]+', 'dollar',emailContent)

  #  print '==========Processed Email==============='
    
     #       res=emailContent.split([' @$/#.-:&*+=[]?!(){},''">_<;%',chr(10),chr(13)])
   # strs='[ @$/#.-:&*+=[]?!(){},''">_<;%'+chr(10)+chr(13)+']+'
    strs=re.split('[ @$/#/-:&*+=?!(){},''"><_;%\n\r]+',emailContent)
    output=[]
    outNum=[]
    for line in strs:
        if line == '':
            continue
        line=re.sub('[^a-zA-Z0-9]', '',line)       
        line=PS.porterStemmer(line.strip())
        
        flag=line in vlist
        if flag:
            item=vlist[line]
            outNum.append(item)
        else:
           # outNum.append(None)
            pass
        output.append(line)
        
        
    strs=' '.join(output)
    print '===================Processed Email Content=========================='
    print '     ',strs
    print ''
    print '==================Word Indiceds for Sample Email===================='
    return outNum


        
        # 
        
    
