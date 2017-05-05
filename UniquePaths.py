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
    def unique_paths(self, m, n):
        if m<0 or n<0:
            return 0
        dp=[[1 for i in range(n)] for j in range(m)]
        for index_row in range(1,m):
            for index_collum in range(1,n):
                dp[index_row][index_collum]=dp[index_row-1][index_collum]+dp[index_row][index_collum-1]
        return(dp[m-1][n-1])
print(Solution().unique_paths(3,3))
