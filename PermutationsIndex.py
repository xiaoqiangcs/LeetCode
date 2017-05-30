import math


class Solution(object):
    def nextPermutation(self, A):
        index = 1
        factor = 1
        for i in range(len(nums) - 1, -1, -1):
            rank = 0
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    rank += 1
            index += rank * factor
            factor *= len(nums) - i
        return index


if __name__ == '__main__':
    nums1 = [1, 2, 3]
    index = Solution().nextPermutation(nums1)
    print(index)