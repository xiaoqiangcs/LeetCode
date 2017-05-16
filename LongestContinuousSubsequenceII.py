'''
Give you an integer matrix (with row size n, column size m)，find the longest increasing continuous subsequence in this matrix. (The definition of the longest increasing continuous subsequence here can start at any row or column and go up/down/right/left any direction).
Example

Given a matrix:
[
  [1 ,2 ,3 ,4 ,5],
  [16,17,24,23,6],
  [15,18,25,22,7],
  [14,19,20,21,8],
  [13,12,11,10,9]
]
return 25
'''
class Soultion (object):
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def maxContinuousSubsequence(self, A):
        if not A or len(A) <1:
            return 0
        dp=[[0 for i in range(len(A[0]))] for j in range (len(A))]
        maxSun = 0
        for row in range(len(A)):
            for column in range(len(A[0])):
                if dp[row][column] == 0:
                    maxSun = max(maxSun, self.ContinuousSubsequence(A, row, column, dp))
        return maxSun
    def ContinuousSubsequence(self, A, row, column, dp):
        # Write your code here
        if dp[row][column]!=0:
            return dp[row][column]
        left = 0
        right = 0
        up = 0
        down = 0
        if row > 0 and A[row-1][column] > A[row][column]:
            left = self.ContinuousSubsequence(A, row-1, column, dp)
        if row+1 < len(A[0]) and A[row+1][column] > A[row][column]:
            right = self.ContinuousSubsequence(A, row+1, column, dp)
        if column > 0 and A[row][column-1] > A[row][column]:
            down = self.ContinuousSubsequence(A, row, column-1, dp)
        if column+1 < len(A) and A[row][column+1] > A[row][column]:
            up = self.ContinuousSubsequence(A, row, column+1, dp)
        dp[row][column] = 1+max(left,right,down, up)
        return dp[row][column]
print(Soultion().maxContinuousSubsequence([[1 ,2 ,3 ,4 ,5],[16,17,24,23,6],[15,18,25,22,7],[14,19,20,21,8],[13,12,11,10,9]]))