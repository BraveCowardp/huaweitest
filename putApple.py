def puta(m,n):
    if m==0 or n==1:
        return 1
    if m<n:
        return puta(m,n-1)
    else:
        return puta(m,n-1)+puta(m-n,n)


while True:
    try:
        str=input().split()
        m=int(str[0])
        n=int(str[1])
        print(puta(m,n))
    except:
        break
