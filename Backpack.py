class Solution(object):
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def Backpack(self, m, A):
        if m<0 or len(A)<=0:
            return -1
        length=len(A)
        result=[[0 for i in range(m+1)] for j in range(len(A)+1)]
        for index_A in range(length):
            for index_m in range(m+1):
                if A[index_A]>index_m:
                    result[index_A+1][index_m]=result[index_A][index_m]
                else:
                    result[index_A+1][index_m]=max(result[index_A][index_m],result[index_A][index_m-A[index_A]]+A[index_A])
        return(result[len(A)][m])
print(Solution().Backpack(5000, [828,125,740,724,983,321,773,678,841,842,875,377,674,144,340,467,625,916,463,922,255,662,692,123,778,766,254,559,480,483,904,60,305,966,872,935,626,691,832,998,508,657,215,162,858,179,869,674,452,158,520,138,847,452,764,995,600,568,92,496,533,404,186,345,304,420,181,73,547,281,374,376,454,438,553,929,140,298,451,674,91,531,685,862,446,262,477,573,627,624,814,103,294,388]))
