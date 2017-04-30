class Solution(object):
    def PartitionArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<0:
            return 0
        left=0
        right=len(nums)-1
        while left<right:
            while nums[left]%2!=0:
                left+=1
            while nums[right]%2==0:
                right-=1
            if left<right:
                nums[left], nums[right]=nums[right],nums[left]
        return nums
print(Solution().PartitionArray([1, 2, 3, 4]))

