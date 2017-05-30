class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 1:
            return nums
        NewSum = sorted(nums)
        result = []
        self.helper(NewSum, result, [])
        return result

    def helper(self, nums, ret, temp):
        if temp[:] not in ret:
            ret.append(temp[:])
        for i, val in enumerate(nums):
            self.helper(nums[i + 1:], ret, temp + [val])


if __name__ == '__main__':
    nums1 = [1, 2, 2]
    index = Solution().subsets(nums1)
    print(index)