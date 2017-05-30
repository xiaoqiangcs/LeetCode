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
        self.helper(NewSum, result, [], [])
        return result

    def helper(self, nums, ret, temp, index):
        if len(temp) == len(nums) and temp not in ret:
            ret.append([] + temp)
        for i, val in enumerate(nums):
            if i not in index:
                index.append(i)
                temp.append(nums[i])
                self.helper(nums, ret, temp, index)
                temp.pop()
                index.pop()


if __name__ == '__main__':
    nums1 = [1, 2, 2, 2]
    index = Solution().subsets(nums1)
    print(index)