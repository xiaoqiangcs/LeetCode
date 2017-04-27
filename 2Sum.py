class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dicresult={}
        for index, number in enumerate(nums):
          if (target-number) in dicresult:
            return index, dicresult[target-number]
          else:
            dicresult[number]=index
