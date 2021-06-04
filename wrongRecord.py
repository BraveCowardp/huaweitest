resList=[]
resDict={}
while(True):
    try:
        str=input().split(' ')
        if str[0]=='':
            break
    except:
        break
    path=str[0]
    lineNum=int(str[1])
    fileName=path.split('\\')[-1]
    if len(fileName)>16:
        fileName=fileName[-16:]
    if (fileName,lineNum) in resDict:
        resDict[(fileName,lineNum)]+=1
    else:
        resDict[(fileName,lineNum)]=1
    if (fileName,lineNum) not in resList:
        if len(resList)<8:
            resList.append((fileName,lineNum))
        if len(resList)>=8 and resDict[(fileName,lineNum)]==1:
            resList.pop(0)
            resList.append((fileName, lineNum))


for i in range(len(resList)):
    group=resList.pop(0)
    print(group[0],group[1],resDict[group])