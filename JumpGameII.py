class Solution (object):
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if len(A) < 0:
            return -1
        start = 0
        end = 0
        jumps = 0
        fastlength = A[0]
        while end < len(A)-1:
            fastlength = end
            for index in range(start, end+1):
                if index+A[index] > fastlength:
                    fastlength = index+A[index]
            if end < fastlength:
                jumps += 1
                start = end+1
                end = fastlength
        return jumps
print(Solution().canJump([2, 3, 1, 1, 4]))