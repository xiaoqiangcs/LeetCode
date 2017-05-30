class Solution(object):
        if A is None or len(A) == 0:
            return 0

        index = 1
        factor = 1
        for i in xrange(len(A) - 1, -1, -1):
            hash_map = {A[i]: 1}
            rank = 0
            for j in xrange(i + 1, len(A)):
                if A[j] in hash_map.keys():
                    hash_map[A[j]] += 1
                else:
                    hash_map[A[j]] = 1
                # get rank
                if A[i] > A[j]:
                    rank += 1

            index += rank * factor / self.dupPerm(hash_map)
            factor *= (len(A) - i)

        return index


    def dupPerm(self, hash_map):
        if hash_map is None or len(hash_map) == 0:
            return 0
        dup = 1
        for val in hash_map.values():
            dup *= self.factorial(val)

        return dup


    def factorial(self, n):
        r = 1
        for i in xrange(1, n + 1):
            r *= i

        return r
if __name__ == '__main__':
    nums1 = [1, 2, 3]
    index = Solution().nextPermutation(nums1)
    print(index)