class Solution(object):
    def removeDuplicates(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(A)<=1:
            return len(A)
        A.sort()
        NewIndex=0
        for i in range(1, len(A)):
            if A[i]!=A[NewIndex]:
                NewIndex+=1
                A[NewIndex]=A[i]
        return NewIndex+
