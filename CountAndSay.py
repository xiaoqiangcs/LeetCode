class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        # write your code here
        if not L:
            return 0
        left, right = 1, max(L)
        while left+1 < right:
            mid = left+int((right-left)/2)
            pieces = sum(int(i / mid) for i in L)
            if pieces < k:
                right = mid
            else:
                left = mid
        if sum(int(i / right) for i in L) >=k:
           return right
        return left
print(Solution().woodCut([2147483644,2147483645,2147483646,2147483647],2))

