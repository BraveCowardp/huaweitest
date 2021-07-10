str=input().split(' ')
allMoney=int(int(str[0])/10)
itemNum=int(str[1])
# price=[[0]]
# value=[[0]]
price={}
value={}
for i in range(1,itemNum+1):
    str=input().split(' ')
    itemPrice=int(int(str[0])/10)
    itemValue=itemPrice*int(str[1])*10
    notMain=int(str[2])
    if notMain:
        price[notMain].append(itemPrice)
        value[notMain].append(itemValue)
    else:
        price[i]=[itemPrice]
        value[i]=[itemValue]
priceList=[[0]]
valueList=[[0]]
index=0
for i in price:
    if len(price[i])==1:
        priceList.append(price[i])
        valueList.append(value[i])
        index+=1
        continue
    if len(price[i])==2:
        priceList.append(price[i])
        valueList.append(value[i])
        index+=1
        priceList[index][1]+=price[i][0]
        valueList[index][1]+=value[i][0]
        continue
    if len(price[i])==3:
        priceList.append(price[i].copy())
        valueList.append(value[i].copy())
        index+=1
        priceList[index][1]+=price[i][0]
        valueList[index][1]+=value[i][0]
        priceList[index][2]+=price[i][0]
        valueList[index][2]+=value[i][0]
        priceList[index].append(price[i][0]+price[i][1]+price[i][2])
        valueList[index].append(value[i][0]+value[i][1]+value[i][2])
dp=[[-1 for _ in range(len(priceList))] for _ in range(allMoney+1)]
for i in range(allMoney+1):
    for j in range(len(priceList)):
        if dp[i][j]!=-1:
            continue
        if i==0 or j==0:
            dp[i][j]=0
            continue
        else:
            maxValue=0
            for k in range(len(priceList[j])):
                maxValue=max(maxValue,dp[i][j-1],dp[i-priceList[j][k]][j-1]+valueList[j][k]) if i-priceList[j][k]>=0 else max(maxValue,dp[i][j-1])
            dp[i][j]=maxValue
print(dp[allMoney][len(priceList)-1])