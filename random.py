numlist = []
inputline=input()
while (inputline != ''):
    N=int(inputline)
    temp = 0
    for i in range(N):
        numlist.append(int(input()))
    numlist.sort()
    for num in numlist:
        if (temp != num):
            print(num)
        temp = num
    numlist.clear()
    inputline=input()