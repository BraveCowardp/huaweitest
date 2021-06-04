import math
num=int(input())
while(True):
    flag=True
    for i in range(2,math.ceil(num**0.5)+1):
        print(i)
        if(num%i==0):
            print(i,end=' ')
            flag=False
            num=num//i
            break
    if(flag):
        print(num,end=' ')
        break