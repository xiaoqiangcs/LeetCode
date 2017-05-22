class Solution(object):
    def mergeSort(self, alist):
        if len(alist)<=1:
            return alist
        mid = int(len(alist) / 2)
        left = self.mergeSort(alist[:mid])
        right = self.mergeSort(alist[mid:])
        return self.sort(left,right)
    def sort(self, left, right):
        length_A = len(left)-1
        length_B = len(right)-1
        index_A, index_B = 0, 0
        result = []
        while index_A<=length_A and index_B <= length_B:
            if left[index_A] <= right[index_B]:
                result.append(left[index_A])
                index_A+=1
            else:
                result.append(right[index_B])
                index_B+=1
        result+=left[index_A:]
        result+=right[index_B:]
        return result
if __name__ == '__main__':
    array = [6, 5, 3, 1, 8, 7, 2, 4]
    index = Solution().mergeSort(array)
    print(index)