class Solution(object):
    def search(self, nums):
        if not nums:
            return -1
        left, right = 0, len(nums)-1
        while left +1 < right:
            mid =left+int((right-left) / 2)
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid
        return min(num[right],nums[left])

if __name__ == '__main__':
    array = [4, 5, 1, 2, 3]
    index = Solution().search(array)
    print(index)