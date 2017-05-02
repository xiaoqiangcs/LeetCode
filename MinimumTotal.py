class Solution(object):
    def minimumTotal(self, triangle):
        n=len(triangle)
        dp=triangle[-1]
        for index in range(n-2,-1,-1):
            for j in range(index+1):
                dp[j]=triangle[index][j]+min(dp[j],dp[j+1])
        return dp[0]

