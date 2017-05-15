'''
Given an array of integers,
find a contiguous subarray which has the largest sum.

Example
Given the array [−2,2,−3,4,−1,2,1,−5,3],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

Note
The subarray should contain at least one number.

Challenge
Can you do it in time complexity O(n)?
'''
class Soultion (object):
    def maxSubArray(self, nums):
        if not nums:
           return -1
        sum = 0
        maxSum = -(2**31-1)
        for index in range(len(nums)):
            sum = max(sum,0)
            sum+=nums[index]
            maxSum = max(maxSum, sum)
        return maxSum
    def maxSubArrayII(self, nums):
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
    def maxSubArrayIII(self, nums):
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
print(Soultion().maxSubArrayII([-2,1,-3,4,-1,2,1,-5,4]))
