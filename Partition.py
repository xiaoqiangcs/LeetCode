class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) <= 1:
            return [s]
        result = []
        self.getpartition(s, 0, result, [])
        return result

    def getpartition(self, nums, pos, result, temp):
        if pos == len(nums):
            result.append([] + temp)
        for index in range(pos, len(nums)):
            if not self.Palindrome(nums[pos:index + 1]):
                continue
            temp.append(nums[pos:index + 1])
            self.getpartition(nums, index + 1, result, temp)
            temp.pop()

    def Palindrome(self, nums):
        if nums is None:
            return None
        if nums == nums[::-1]:
            return True
        else:
            return False


if __name__ == '__main__':
    index = Solution().partition("aab")
    print(index)