resDict={'A':0,'B':0,'C':0,'D':0,'E':0,'Wrong':0,'Private':0}

def subCodeWrongHandle(subCodeStr):
    try:
        subCodeList=list(map(int,subCodeStr.split('.')))
        for i in range(4):
            if subCodeList[i]<0 or subCodeList[i]>255:
                resDict['Wrong'] += 1
                return True
        subCodeBinstr=''
        for subCode in subCodeList:
            subCodeBinstr+='{:08b}'.format(subCode)
        if subCodeBinstr.find('0')!=subCodeBinstr.rfind('1')+1:
            resDict['Wrong'] += 1
            return True
        return False
    except:
        resDict['Wrong']+=1
        return True


def ipWrongHandle(ipStr):
    try:
        ipList=list(map(int,ipStr.split('.')))
        for i in range(4):
            if ipList[i]<0 or ipList[i]>255:
                resDict['Wrong'] += 1
                return True
        return False
    except:
        resDict['Wrong']+=1
        return True

def findClass(ipStr):
    ipList = list(map(int, ipStr.split('.')))
    if ipList[0]>=1 and ipList[0]<=126:
        resDict['A']+=1
        return
    if ipList[0]>=128 and ipList[0]<=191:
        resDict['B']+=1
        return
    if ipList[0]>=192 and ipList[0]<=223:
        resDict['C']+=1
        return
    if ipList[0]>=224 and ipList[0]<=239:
        resDict['D']+=1
        return
    if ipList[0]>=240 and ipList[0]<=255:
        resDict['E']+=1
        return

def findPrivate(ipStr):
    ipList = list(map(int, ipStr.split('.')))
    if ipList[0]==10:
        resDict['Private']+=1
        return
    if ipList[0]==172 and ipList[1]>=16 and ipList[1]<=31:
        resDict['Private']+=1
        return
    if ipList[0]==192 and ipList[1]==168:
        resDict['Private']+=1
        return

while(True):
    try:
        str=input().split('~')
    except:
        break
    if str[0]=='':
        break
    ipStr=str[0]
    subCodeStr=str[1]
    if ipWrongHandle(ipStr):
        continue
    if subCodeWrongHandle(subCodeStr):
        continue
    findClass(ipStr)
    findPrivate(ipStr)

print(resDict['A'],end=' ')
print(resDict['B'],end=' ')
print(resDict['C'],end=' ')
print(resDict['D'],end=' ')
print(resDict['E'],end=' ')
print(resDict['Wrong'],end=' ')
print(resDict['Private'],end=' ')