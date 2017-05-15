'''
Given an array of integers,
find two non-overlapping subarrays which have the largest sum.

The number in each subarray should be contiguous.

Return the largest sum.

Example
For given [1, 3, -1, 2, -1, 2],
the two subarrays are [1, 3] and [2, -1, 2] or [1, 3, -1, 2] and [2],
they both have the largest sum 7.

Note
The subarray should contain at least one number

Challenge
Can you do it in time complexity O(n)
'''
class Soultion (object):
    def maxSubArray(self, nums):
        if not nums:
            return -1
        maxSum = -(2**31-1)
        for index in range(1,len(nums)):
            Currensum = self.maxSub(nums[:index+1])+self.maxSub(nums[index+1:])
            maxSum = max(maxSum, Currensum)
        return maxSum
    def maxSub(self, nums):
        if not nums:
           return -1
        sum = 0
        maxSum = -(2**31-1)
        minSum = (2**31-1)
        for index in range(len(nums)):
            minSum = min(minSum, sum)
            sum+=nums[index]
            maxSum = max(maxSum, sum-minSum)
        return maxSum
print(Soultion().maxSubArray([1, 3, -1, 2, -1, 2]))
