
def findWayNum(dpList,x,y):
    if dpList[x][y]!=-1:
        return dpList[x][y]
    if x==0:
        dpList[x][y]=findWayNum(dpList,x,y-1)
        return dpList[x][y]
    elif y==0:
        dpList[x][y]=findWayNum(dpList,x-1,y)
        return dpList[x][y]
    else:
        dpList[x][y]=findWayNum(dpList,x,y-1)+findWayNum(dpList,x-1,y)
        return  dpList[x][y]


while(True):
    try:
        str=input()
        if str=='':
            break
    except:
        break
    str=str.split(' ')
    n=int(str[0])+1
    m=int(str[1])+1
    dpList=[[-1 for i in range(m)] for j in range(n)]
    dpList[0][0]=1
    print(findWayNum(dpList,n-1,m-1))