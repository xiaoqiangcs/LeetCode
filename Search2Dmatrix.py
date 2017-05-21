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
        row, colmu  = 0, len(matrix[0])-1
        corrent = 0
        while row < len(matrix) and colmu >= 0:
            if matrix[row][colmu] == target:
                corrent+=1
                colmu-=1
            elif matrix[row][colmu] < target:
                row+=1
            else:
                colmu-=1
        return corrent
if __name__ == '__main__':
    array = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    index = Solution().searchMatrix(array, 3)
    print(index)