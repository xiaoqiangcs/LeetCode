class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None:
            return [[]]
        elif len(nums) <= 1:
            return nums
        # Find the first nums[k]<nums[k+1]
        for index in range(len(nums) - 2, -1, -1):
            if nums[index] > nums[index + 1]:
                break
            elif index == 0:
                return nums[::-1]
        #Finde the first one j nums[j]>nums[index]
        for j in range(len(nums) - 1, index, -1):
            if nums[j] < nums[index]:
                break
        #Exchange the num[j]，nums[index]
        nums[j], nums[index] = nums[index], nums[j]
        nums[index + 1:] = nums[len(nums) - 1:index:-1]
        return nums


if __name__ == '__main__':
    nums1 = [1,3,2,3]
    index = Solution().nextPermutation(nums1)
    print(index)