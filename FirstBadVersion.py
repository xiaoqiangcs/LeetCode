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
        """
    @param n: An integers.
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        if n<1:
            return 0
        left, right = 1, n+1
        while left+1 < right:
            mid = int((right+left)/2)
            if VersionControl.isBadVersion(mid):
                right = mid
            else:
                left = mid
        return left+1
if __name__ == '__main__':
    array = [0,0,0,1,2,3]
    index = Solution().findFirstBadVersion(5)
    print(index)
