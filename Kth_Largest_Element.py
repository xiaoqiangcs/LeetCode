class Solution(object):
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self,k, A):
        if k==0 or len(A)==0:
            return ''
        kth=self.qsort(A,0,len(A)-1,k)
        return kth
    def qsort(self,Array,left,Right,kth):
        print(Array)
        if left>Right:
            return Array[Right]
        index=left
        for i in range(left+1, Right+1):
            if Array[i]>Array[left]:
                index+=1
                Array[index],Array[i]=Array[i],Array[index]
        Array[index],Array[left]=Array[left],Array[index]
        if index+1==kth:
            return Array[index]
        elif index+1>kth:
            return(self.qsort(Array,left,index-1,kth))
        else:
            return(self.qsort(Array,index+1,Right,kth))
print(Solution().kthLargestElement(10,[1,2,3,4,5,6,8,9,10,7]))
