class Solution(object):
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def climbStairs(self, n):
        if n < 1:
            return 0
        l = r = 1
        for __ in range(n - 1):
            l, r = r, r + l
        return r
print(Solution().climbStairs(3))
