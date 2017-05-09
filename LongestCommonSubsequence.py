class Solution (object):
    def longestCommonSubsequence(self, A, B):
        if not A or not B:
            return 0
        length=[[0 for j in range (len(B)+1)] for i in range (len(A)+1)]
        for i in range(1,1+len(A)):
            for j in  range(1,1+len(B)):
                if A[i-1]==B[j-1]:
                    length[i][j]=1+length[i-1][j-1]
                else:
                    length[i][j]=max(length[i-1][j],length[i][j-1])
        return length[len(A)][len(B)]