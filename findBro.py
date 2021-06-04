def getDict(word):
    tempdict={}
    letterList=list(word)
    letterList.sort()
    for c in letterList:
        if c in tempdict:
            tempdict[c]+=1
        else:
            tempdict[c]=1
    return tempdict


