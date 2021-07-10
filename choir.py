while True:
    try:
        Num=int(input())
        heightList=list(map(int,input().split()))
    except:
        break
    leftList=[]
    rightList=[]
    dpLeft=[1 for _ in range(len(heightList)+1)]
    dpRight=[1 for  _ in range(len(heightList)+1)]
    for i in range(1,len(heightList)+1):
        for j in range(1,i):
            if heightList[j-1]<heightList[i-1] and dpLeft[j]+1>dpLeft[i]:
                dpLeft[i]=dpLeft[j]+1
    heightList.reverse()
    for i in range(1,len(heightList)+1):
        for j in range(1,i):
            if heightList[j-1]<heightList[i-1] and dpRight[j]+1>dpRight[i]:
                dpRight[i] = dpRight[j] + 1
    dpRight.reverse()
    for i in range(1,len(heightList)+1):
        dpLeft[i]+=dpRight[i-1]-1
    print(Num-max(dpLeft))