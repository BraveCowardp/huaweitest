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

str=input()
strList=str.split(' ')
dictSize=int(strList[0])
wordList=strList[1:-2]
originWord=strList[-2]
k=int(strList[-1])

wordDictList=list(map(getDict,wordList))
originWordDict=getDict(originWord)
indexList=[]
resNum=0
broWordList=[]

for i in range(len(wordDictList)):
    if wordDictList[i]==originWordDict and wordList[i]!=originWord:
        indexList.append(i)
        resNum+=1

for i in range(resNum):
    broWordList.append(wordList[indexList[i]])

broWordList.sort()
print(resNum)
if k <= resNum:
    print(broWordList[k-1])