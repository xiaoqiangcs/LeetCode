class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        if not (A and B):
            return 0
        lcs = 0
        for i in range(len(A)):
            for j in range(len(B)):
                lcs_temp = 0
                while (i + lcs_temp < len(A) and
                       j + lcs_temp < len(B) and
                       A[i + lcs_temp] == B[j + lcs_temp]):
                    lcs_temp += 1
                # update lcs
                if lcs_temp > lcs:
                    lcs = lcs_temp
        return lcs
