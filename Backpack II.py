#Given n items with size AiAi and value Vi, and a backpack with size m.
#What's the maximum value can you put into the backpack?
class Solution(object):
    # @param m: An integer m denotes the size of a backpack
    # @param A & V: Given n items with size A[i] and value V[i]
    # @return: The maximum value
    def Backpack(self, m, A, V):
        if m<0 or len(A)<=0:
            return -1
        length=len(A)
        result=[[0 for i in range(m+1)] for j in range(len(A)+1)]
        for index_A in range(length):
            for index_m in range(m+1):
                if A[index_A]>index_m:
                    result[index_A+1][index_m]=result[index_A][index_m]
                else:
                    result[index_A+1][index_m]=max(result[index_A][index_m],result[index_A][index_m-A[index_A]]+V[index_A])
        return(result[len(A)][m])
print(Solution().Backpack(10, [2, 3, 5, 7], [1, 5, 2, 4]))
#O(n x m) memory
