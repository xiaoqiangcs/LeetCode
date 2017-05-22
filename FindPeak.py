"""
Problem Statement

The code base version is an integer start from 1 to n. One day, someone committed a bad version in the code case, so it caused this version and the following versions are all failed in the unit tests. Find the first bad version.
You can call isBadVersion to help you determine which version is the first bad one. The details interface can be found in the code's annotation part.
Example

Given n = 5:
isBadVersion(3) -> false
isBadVersion(5) -> true
isBadVersion(4) -> true
Here we are 100% sure that the 4th version is the first bad version.
"""


class Solution(object):
    def findPeakElement(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not A:
            return -1

        l, r = 0, len(A) - 1
        while l + 1 < r:
            mid = l + (r - l) / 2
            if A[mid] < A[mid - 1]:
                r = mid
            elif A[mid] < A[mid + 1]:
                l = mid
            else:
                return mid
        mid = l if A[l] > A[r] else r
        return mid
if __name__ == '__main__':
    array = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    index = Solution().searchMatrix(array, 3)
    print(index)