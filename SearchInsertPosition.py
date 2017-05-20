"""
Problem Statement

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume NO duplicates in the array.
Example

[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""
class  Solution(object):
    def seachInsert(self, A, target):
        if not A or not target:
            return 0
        left, right = 0, len(A)-1
        while left +1 < right:
            mid = int((left+right) / 2)
            if A[mid] == target:
                return mid
            elif target < A[mid]:
                right = mid
            else:
                left = mid
        if A[left] >= target:
            return left
        elif A[right] >= target:
            return right
        else:
            return len(A)
if __name__ == '__main__':
    array = [1,3,5,6]
    index = Solution().seachInsert(array,5)
    print(index)
