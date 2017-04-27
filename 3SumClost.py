class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)<3:
          return -1
        nums.sort()
        BestValue=nums[0]+nums[1]+nums[2]
        for index in range(len(nums)):
          start=index+1
          end=len(nums)-1
          while start<end:
            Curren_sum=nums[index]+nums[start]+nums[end]
            if abs(Curren_sum-target)<abs(BestValue-target):
              BestValue=Curren_sum
            else:
              if Curren_sum<target:
                start+=1
              else:
                end-=1
        return BestValue
