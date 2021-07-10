import math
from typing import List
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        allWeight=0
        for weight in stones:
            allWeight+=weight
        halfWeight=math.floor(allWeight/2)
        dp=[[-1 for _ in range(len(stones)+1)] for _ in range(halfWeight+1)]
        for i in range(halfWeight+1):
            for j in range(len(stones)+1):
                if dp[i][j]>=0:
                    continue
                if i==0 or j==0:
                    dp[i][j]=0
                    continue
                if i>0 and j>0:
                    dp[i][j]=max(dp[i][j-1],dp[i-stones[j-1]][j-1]+stones[j-1]) if i-stones[j-1]>=0 else dp[i][j-1]
        lessWeight=dp[halfWeight][len(stones)]

        return allWeight-2*lessWeight