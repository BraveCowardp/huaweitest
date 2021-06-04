letterSet={chr(i) for i in range(ord('a'),ord('z')+1)}.union(chr(i) for i in range(ord('A'),ord('Z')+1))
str=input()
wordList=[]
tempWord=''
wordFlag=False
for c in str:
    if c in letterSet:
        tempWord+=c
        wordFlag=True
    elif wordFlag:
        wordList.append(tempWord)
        tempWord=''
if wordFlag:
    wordList.append(tempWord)
    tempWord = ''
for i in range(len(wordList)):
    print(wordList.pop(),end=' ')