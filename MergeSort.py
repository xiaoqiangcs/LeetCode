class Solution(object):
    def findMedianSortedArrays(self, A, B):
        length = len(A) + len(B)
        median_index = int(length / 2)
        if length % 2 == 1:
            return (self.findKth(A, B, median_index+1))
        else:
            return ((self.findKth(A, B, median_index) + self.findKth(
                A, B, median_index + 1)) / 2.0)

    def findKth(self, A, B, k):
        if len(A) == 0:
            return B[k - 1]
        if len(B) == 0:
            return A[k - 1]
        if k == 1:
            return min(A[0], B[0])
        mid_length = int(k / 2)
        if len(A) >= mid_length:
            mid_A = A[mid_length - 1]
        else:
            mid_A = None
        if len(B) >= mid_length:
            mid_B = B[mid_length - 1]
        else:
            mid_B = None
        if mid_B is None or (mid_A and mid_A < mid_B):
            return self.findKth(A[mid_length:], B, k - mid_length)
        else:
            return self.findKth(A, B[mid_length:], k - mid_length)
if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3]
    index = Solution().findMedianSortedArrays(nums1, nums2)
    print(index)