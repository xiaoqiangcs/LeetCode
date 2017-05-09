class Solution (object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        length = [1 for i in range(len(nums))]
        for index in range(1, len(nums)):
            for i in range(index):
                if nums[i] < nums [index] and length[index] < 1+ length [i]:
                    length[index] = 1+length[i]
        return max(length)
print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))