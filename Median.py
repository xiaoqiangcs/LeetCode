class Solution(object):
    def FindMedian(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return -1
        return self.qsort(nums,0,len(nums)-1, (1 + len(nums)) / 2)
    def qsort(self,nums,left,right,k):
        if left>right:
            return nums[right]
        index=left
        for i in range(left+1,right+1):
            if left >= right:
                return nums[right]
            if nums[i]<nums[left]:
                index+=1
                nums[index],nums[i]=nums[i],nums[index]
        nums[index],nums[left]=nums[left],nums[index]
        if k==index+1:
            return nums[index]
        elif k>index+1:
            return self.qsort(nums,index+1,right,k)
        else:
            return self.qsort(nums,left,index-1,k)
print(Solution().FindMedian([4, 5, 1, 2]))

