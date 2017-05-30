class Solution(object):
    """
    @param n: n
    @param k: the k-th permutation
    @return: a string, the k-th permutation
    """

    def getPermutation(self, n, k):
        sequence = [i for i in range(1, n + 1)]
        index = 1
        for _ in range(1, k):
            i = 0
            for i in range(n - 2, -1, -1):
                if sequence[i] < sequence[i + 1]:
                    break
            index = 0
            for index in range(n - 1, i, -1):
                if sequence[index] > sequence[i]:
                    break
            sequence[i], sequence[index] = sequence[index], sequence[i]
            sequence[i + 1:] = sequence[n - 1:i:-1]
            index += 1
        result = ""
        for j in sequence:
            result += str(j)
        return result

    def getPermutationII(self, n, k):
        fact = [1]
        for index in range(1, n + 1):
            fact.append(fact[-1] * index)
        nums = list(range(1, n + 1))
        result = []
        for i in range(1, n + 1):
            number = int((k - 1)/ fact[n - i])
            result.append(nums[number])
            k = (k - 1) % fact[n - i] + 1
            nums.remove(nums[number])
        return result


if __name__ == '__main__':
    index = Solution().getPermutationII(3, 2)
    print(index)