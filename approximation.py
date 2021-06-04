import math
fnum=float(input())
inum=math.floor(fnum)
num=inum+1 if fnum-inum>=0.5 else inum
print(num)