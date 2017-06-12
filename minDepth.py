class Solution(object):
    """
    Given a collection of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.
Each number in C may only be used once in the combination.

Have you met this question in a real interview? Yes
Example
For example, given candidate set 10,1,6,7,2,1,5 and target 8,

A solution set is:

[1,7]

[1,2,5]

[2,6]

[1,1,6]

Note
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order.
(ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
    """

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if candidates is None:
            return None
        res = []
        candidates = sorted(candidates)
        self.help(candidates, 0, target, res, [])
        return res

    def help(self, candidates, pos, gap, res, temp):
        if gap == 0 and temp not in res:
            res.append([] + temp)
            return
        for index in range(pos, len(candidates)):
            if gap < candidates[index]:
                return
            temp.append(candidates[index])
            self.help(candidates, index + 1, gap - candidates[index], res,
                      temp)
            temp.pop()


if __name__ == '__main__':
    index = Solution().combinationSum2([10, 1, 6, 7, 2, 1, 5], 8)
    print(index)