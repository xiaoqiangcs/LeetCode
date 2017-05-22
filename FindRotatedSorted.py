class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left, right = 0, len(nums)-1
        while left + 1 < right:
            print(left)
            mid = left + int((right - left) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[left]:
                if nums[left] <= target and target <= nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] <= target and target <= nums[right]:
                    left = mid
                else:
                    right = mid
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1


if __name__ == '__main__':
    array = [4, 5, 1, 2, 3]
    index = Solution().search(array)
    print(index)