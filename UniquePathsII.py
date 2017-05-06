#A robot is located at the top-left corner of a m x n grid
#(marked 'Start' in the diagram below).
#The robot can only move either down or right at any point in time.
#The robot is trying to reach the bottom-right corner of the grid
#(marked 'Finish' in the diagram below).

#How many possible unique paths are there?

#Note:m and n will be at most 100.
class Solution(object):
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def unique_paths(self, obstacleGrid):
        if len(obstacleGrid)<0:
            return 0
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            if obstacleGrid[i][0]==0:
                dp[i][0]=1
            else:
                break
        for i in range(n):
            if obstacleGrid[0][i]==0:
                dp[0][i]=1
            else:
                break
        for index_row in range(1,m):
            for index_collum in range(1,n):
                if obstacleGrid[index_row][index_collum]==0:
                    dp[index_row][index_collum]=dp[index_row-1][index_collum]+dp[index_row][index_collum-1]
                else:
                    dp[index_row][index_collum]=0
                print(dp[index_row][index_collum])
        return(dp[m-1][n-1])
print(Solution().unique_paths([[0,0],[0,0],[0,0],[1,0],[0,0]]))