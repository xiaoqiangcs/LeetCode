#A robot is located at the top-left corner of a m x n grid
#Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#Note
#You can only move either down or right at any point in time.
class Solution(object):
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def _minimum_path_sum(self,triangle):
        if len(triangle)<0:
            return -1
        row=len(triangle)
        collum=len(triangle[0])
        dp=[1000 for __ in range(collum)]
        dp[0]=0
        for index_row in range(row):
            dp[0]=dp[0]+triangle[index_row][0]
            for index_collum in range(1,collum):
                dp[index_collum]=triangle[index_row][index_collum]+min(dp[index_collum-1],dp[index_collum])
                print(dp)
        return (dp[collum-1])
print(Solution()._minimum_path_sum([[1,3,1],[1,5,1],[4,2,1]]))
