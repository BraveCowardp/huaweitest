from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        countList = [[0,0]]
        listLen=len(strs)
        for str in strs:
            countList.append([str.count('0'), str.count('1')])
        dp=[[[-1 for i in range(listLen+1)] for j in range(n+1)] for k in range(m+1)]
        dp[0][0]=[0 for i in range(listLen+1)]
        for i in range(m+1):
            for j in range(n+1):
                for k in range(listLen+1):
                    if dp[i][j][k]>-1:
                        continue
                    if i-countList[k][0]>=0 and j-countList[k][1]>=0:
                        dp[i][j][k]=max(dp[i][j][k-1],dp[i-countList[k][0]][j-countList[k][1]][k-1]+1)
                        continue
                    else:
                        dp[i][j][k]=dp[i][j][k-1]
        return dp[m][n][listLen]


solution=Solution()

res=solution.findMaxForm(["10","0001","111001","1","0"],5,3)
print(res)