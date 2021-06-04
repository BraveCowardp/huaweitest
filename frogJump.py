'''
一维简单DP
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''

jumpnum=[1,2]

def findjumpnum(n):
    if n<=len(jumpnum):
        return jumpnum[n-1]
    else:
        jumpnum.append(jumpnum[n-2]+jumpnum[n-3])
        return jumpnum[n-1]

print(findjumpnum(3))