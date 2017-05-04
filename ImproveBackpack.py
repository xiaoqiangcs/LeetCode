class Solution(object):
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def Backpack(self, m, A):
        if m<0 or len(A)<=0:
            return -1
        length=len(A)
        result=[0 for i in range(m+1)]
        for index_A in range(length):
            for index_m in range(m,-1,-1):
                if A[index_A]<index_m:
                    temp=result[index_m-A[index_A]]+A[index_A]
                    result[index_m]=max(result[index_m], temp)
        return(result[m])
print(Solution().Backpack(11, [2, 3, 5, 7]))
