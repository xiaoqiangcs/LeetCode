"""
Problem Statement

Given a sorted array of n integers, find the starting and ending position of a given target value.
If the target is not found in the array, return [-1, -1].
Example

Given [5, 7, 7, 8, 8, 10] and target value 8, return [3, 4].
Challenge

O(log n) time.
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or not target:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        index = [-1,-1]
        while left < right:
            if nums[left] == target and index[0]== -1:
                index[0] = left
            if nums[left] < target:
                left += 1
            if nums[right] == target and index[1]== -1:
                index[1] = right
            if nums[right] > target:
                right -= 1
            if index[0]!=-1 and index[1]!=-1:
                break
        print(index)
        if index[0] == -1:
            return [index[1],index[1]]
        elif index[1] == -1:
            return [index[0],index[0]]
        else:
            return index
if __name__ == '__main__':
    array = [0,0,0,1,2,3]
    index = Solution().searchRange(array, 0)
    print(index)
