'''
Problem Statement

Give you an integer array (index from 0 to n-1, where n is the size of this array)，find the longest increasing continuous subsequence in this array. (The definition of the longest increasing continuous subsequence here can be from right to left or from left to right)
Example

For [5, 4, 2, 1, 3], the LICS is [5, 4, 2, 1], return 4.
For [5, 1, 2, 3, 4], the LICS is [1, 2, 3, 4], return 4.
Note

O(n) time and O(1) extra space.
'''
class Soultion (object):
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def maxContinuousSubsequence(self, A):
        if not A:
            return -1
        dp = [0]*len(A)
        maxSun = 0
        for index in range(len(A)):
            if dp[index] == 0:
                maxSun = max(maxSun, self.ContinuousSubsequence(A, index, dp))
        return maxSun
    def ContinuousSubsequence(self, A, i,dp):
        # Write your code here
        if not A:
            return -1
        if dp[i]!=0:
            return dp[i]
        left = 0
        righ = 0
        if i > 0 and A[i-1] > A[i]:
            left = self.ContinuousSubsequence(A, i-1, dp)
        if i+1 < len(A) and A[i+1] > A[i]:
            righ = self.ContinuousSubsequence(A, i+1, dp)
        dp[i] = 1+ max(left, righ)
        return dp[i]
print(Soultion().maxContinuousSubsequence([5, 4, 2, 1,0, 3]))