# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 10:24:10 2016

@author: aa
"""

def porterStemmer(line):
    line=line.lower()
    b=line
    k=len(b)-1
    k0=0
    global j
    j=k
    stem=b
    
    def cons(i,b,k0):
        ''' cons is true if b[i] is consonant.'''
        c=True
        dicts={'a':False,'e':False,'i':False,'o':False,'u':False,'y':True}
        flag=b[i] in dicts.keys()
        if ~flag :
            return True
        if ~dicts[b[i]]:
            return False
        if i == k0:
            return True
        c=~cons(i-1,b,k0)
        return c

   
    def m(b,k0):
        ''' measure the frequence'''
        n=0
        i=k0
        while True:
            if i >= j:
                return n
            if ~cons(i,b,k0):
                break
            i = i+1
        i = i +1
        while True:
            while True:
                if i >= j:
                    return n
                if cons(i,b,k0):
                    break
                i = i +1
            i = i +1
            n = n +1
            while True:
                if i >= j:
                    return n
                if ~cons(i,b,k0):
                    break
                i = i +1
            i = i +1
    
    def vowelinstem(b,k0):
        ''' vowelinstem is True if k0... j contains a vowel. '''
        for i in range(j+1):
            if ~cons(i,b,k0):
                return True
        return False
    
    def doublec(i,b,k0):
        ''' boublec[i] is true if i,(i-1) contains a double consonant. '''
        if i < k0+1:
            return False       
        if b[i] != b[i-1]:
            return False
        return cons(i,b,k0)
        
    
    def cvc(i,b,k0):
        """cvc(i) is TRUE <=> i-2,i-1,i has the form consonant - vowel - consonant
        and also if the second c is not w,x or y. this is used when trying to
        restore an e at the end of a short  e.g.

           cav(e), lov(e), hop(e), crim(e), but
           snow, box, tray.
        """
        flag=(i < k0+2) or (~cons(i,b,k0)) or (cons(i-1,b,k0)) or (~cons(i-2,b,k0))
        if flag:
            return False
        else:
            if (b[i] == 'w') or (b[i] == 'x') or (b[i] == 'y'):
                return False
            return True
     
    def ends(strs,b,k):
        """ends(s) is TRUE <=> k0,...k ends with the string strs."""
        global j
        length=len(strs)
        if strs[length-1] != b[k]:
            return False
        if len(strs)>k+1:
            return False
        if b[k-length+1:k+1] == strs:
            j=k-length
            return True
        return False
        
        
    def setto(strs,b):
         """setto(s) sets (j+1),...k to the characters in the string s, readjusting k."""
         global j
         length=len(strs)
         b = b[:j+1] + strs+b[j+length+1:]
         k = len(b)
         return (b,k)
         
     
    def rs(strs,b,k,k0):
        """r(s) is used further down."""
        if m(b,k0) > 0:
            return setto(strs,b)
        return (b,k)

# 
    def step1AB(b,k,k0):
        """step1ab() gets rid of plurals and -ed or -ing. e.g."""
        global j
        if b[k] == 's':
           if ends('sses',b,k):
               k = k -2
           elif ends('ies',b,k):
               retVal=setto('i',b)       
               b=retVal[0]
               k=retVal[1]
           elif b[k-1] != 's':
               k = k -1
        if ends('eed',b,k):
            if m(b,k0)> 0:
                k = k -1
        elif ((ends('ed',b,k)) or (ends('ing',b,k))) and (vowelinstem(b,k0)):
            k=j
            retVal=(b,k)
            if ends('at',b,k):
                retVal=setto('ate',b[k0:k])
            elif ends('bl',b,k):
                retVal=setto('ble',b[k0:k])
            elif ends('iz',b,k):
                retVal=setto('ize',b[k0:k])
            elif doublec(k,b,k0):
                retVal=(b,k-1)
                if b[k-1] == 'l' or b[k-1] == 's' or b[k-1] == 'z':
                    retVal=(retVal[0],k)
            elif m(b,k0) == 1 and cvc(k,b,k0):
                retVal=setto('e',b[k0:k])
            k=retVal[1]
            b=retVal[0][k0:k+1]
        j=k
        return (b,k)       
  
    
    def step1C(b,k,k0):
        """step1c() turns terminal y to i when there is another vowel in the stem."""
        global j
        
        if ends('y',b,k) and vowelinstem(b,k0):
            b=b[:k]+'i'+b[k+1:]
        j=k
        return (b,k)
     
    def step2(b,k,k0):
        """step2() maps double suffices to single ones.
        so -ization ( = -ize plus -ation) maps to -ize etc. note that the
        string before the suffix must give m() > 0.
        """
        global j
        res=(b,k)
        if b[k-1]== 'a':
            if ends('actional',b,k):
                res= rs('ate',b,k,k0) 
            elif ends('tional',b,k):
                res= rs('tion',b,k,k0)
        elif b[k-1]== 'c':
            if ends('enci',b,k):
                res= rs('ence',b,k,k0)
            elif ends('anci',b,k):
                res= rs('ance',b,k,k0)
        elif b[k-1]== 'e':
            if ends('izer',b,k):
                res= rs('ize',b,k,k0)        
        elif b[k-1]=='l':
            if ends('bli',b,k):
                res= rs('ble',b,k,k0)
            elif ends('alli',b,k):
                res= rs('al',b,k,k0)
            elif ends('entli',b,k):
                res= rs('ent',b,k,k0)
            elif ends('eli',b,k):
                res= rs('e',b,k,k0)
            elif ends('outsli',b,k):
                res= rs('ous',b,k,k0)            
        elif b[k-1]== 'o':
            if ends('ization',b,k):
                res= rs('ize',b,k,k0)
            elif ends('action',b,k):
                res= rs('ate',b,k,k0)
            elif ends('ator',b,k):
                res= rs('ate',b,k,k0)          
        elif b[k-1]=='s':
            if ends('alism',b,k):
                res= rs('al',b,k,k0)
            elif ends('iveness',b,k):
                res= rs('ive',b,k,k0)
            elif ends('fulness',b,k):
                res= rs('ful',b,k,k0)
            elif ends('ousness',b,k):
                res= rs('ous',b,k,k0)
        elif b[k-1]== 't':
            if ends('aliti',b,k):
                res= rs('al',b,k,k0)
            elif ends('iviti',b,k):
                res= rs('ive',b,k,k0)
            elif ends('biliti',b,k):
                res= rs('ble',b,k,k0)
        elif b[k-1]=='g':
            if ends('logi',b,k):
                res= rs('log',b,k,k0)
        j=res[1]
        return res

    
    def step3(b,k,k0):
        """step3() dels with -ic-, -full, -ness etc. similar strategy to step2."""
        global j
        res=(b,k)
        if b[k]== 'e':
            if ends('icate',b,k):
                res=rs('ic',b,k,k0)
            elif ends('ative',b,k):
                res=rs('',b,k,k0)
            elif ends('alize',b,k):
                res=rs('al',b,k,k0)
        elif b[k]== 'i':
            if ends('iciti',b,k):
                res=rs('ic',b,k,k0)
        elif b[k]== 'l':
            if ends('ical',b,k):
                res=rs('ic',b,k,k0)
            elif ends('ful',b,k):
                res=rs('',b,k,k0)
        elif b[k]== 's':
            if ends('ness',b,k):
                res=rs('',b,k,k0)
        j=res[1]
        return res
        
    def step4(b,k,k0):
        """step4() takes off -ant, -ence etc., in context <c>vcvc<v>."""
        global j
        if b[k-1] == 'a':
            if ends('al',b,k):
                pass
        elif b[k-1]=='c':
            if ends('ance',b,k):
                pass
            elif ends('ence',b,k):
                pass
        elif b[k-1]== 'e':
            if ends('er',b,k):
                pass
        elif b[k-1]=='i':
            if ends('ic',b,k):
                pass
        elif b[k-1]== 'l':
            if ends('able',b,k):
                pass
            elif ends('ible',b,k):
                pass
        elif b[k-1]== 'n':
            if ends('ant',b,k):
                pass
            elif ends('ement',b,k):
                pass
            elif ends('ment',b,k):
                pass
            elif ends('ent',b,k):
                pass
        elif b[k-1]=='o':
            if ends('ion',b,k):
                if j == 0:
                    pass
                elif ~((b[j] == 's') or (b[j] == 't')):
                    j=k
            elif ends('ou',b,k):
                pass
        elif b[k-1]=='s':
            if ends('ism',b,k):
                pass
        elif b[k-1]=='t':
            if ends('ate',b,k):
                pass
            elif ends('iti',b,k):
                pass
        elif b[k-1]=='u':
            if ends('ous',b,k):
                pass
        elif b[k-1]=='v':
            if ends('ive',b,k):
                pass
        elif b[k-1]=='z':
            if ends('ize',b,k):
                pass
        
        if m(b,k0) > 1:
            res=(b[k0:j+1],j)
        else:
            res=(b[k0:k+1],k)  
        return res
        
        
    
    def step5(b,k,k0):
        """step5() removes a final -e if m() > 1, and changes -ll to -l if
        m() > 1.
        """
        global j
        j=k
        if b[k]== 'e':
            a=m(b,k0)
            if (a > 1) or ((a == 1)  and ~cvc(k-1,b,k0)):
                k=k-1
        if b[k] == 'l' and doublec(k,b,k0) and m(b,k0)> 1:
            k = k-1
        res = (b[k0:k+1],k)
        return res

# ====================Main Content======================
    if k > 2:
        x=step1AB(b,k,k0)
        x=step1C(x[0],x[1],k0)
        x=step2(x[0],x[1],k0)
        x=step3(x[0],x[1],k0)
        x=step4(x[0],x[1],k0)
        x=step5(x[0],x[1],k0)
        stem=x[0]
    return stem
    
