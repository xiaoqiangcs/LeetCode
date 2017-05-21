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
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        row_length = len(matrix)
        column_length = len(matrix[0])
        down, up = -1, row_length
        while down + 1 < up:
            mid = down + int((up - down) / 2)
            if matrix[mid][column_length - 1] < target:
                down = mid
            else:
                up = mid
        column_target = down + 1
        print(column_target)
        if column_target >= row_length:
            return False
        left, right = -1, column_length
        while left + 1 < right:
            mid = left + int((right - left) / 2)
            if matrix[column_target][mid] < target:
                left = mid
            else:
                right = mid
        row_target = left + 1
        print(row_target)
        if row_target >= column_length:
            return False
        if (matrix[column_target][row_target] == target):
            return True
        else:
            return False

if __name__ == '__main__':
    array = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    index = Solution().searchMatrix(array, 55)
    print(index)