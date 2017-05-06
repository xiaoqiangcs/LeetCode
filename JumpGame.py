class Solution (object):
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if len(A) < 0:
            return -1
        fastlength = A[0]
        for index in range(1, len(A)):
            if index < fastlength and index+A[index] > fastlength:
                fastlength = index+A[index]
        return fastlength > len(A)-1
print(Solution().canJump([3, 2, 1, 0, 4]))
