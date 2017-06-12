class Solution(object):
    """
    Problem Statement

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
Example

For example, If n = 4 and k = 2, a solution is: [[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]]
    """

    def combinationSum(self, candidates, target):
        # write your code her
        if candidates is None:
            return None
        res = []
        candidates = sorted(candidates)
        self.help(candidates, 0, target, res, [])
        return res

    def help(self, candidates, pos, gap, res, temp):
        if gap == 0:
            res.append([] + temp)
            return
        for index in range(pos, len(candidates)):
            if gap < candidates[index]:
                return
            temp.append(candidates[index])
            self.help(candidates, index, gap - candidates[index], res, temp)
            temp.pop()


if __name__ == '__main__':
    index = Solution().combinationSum([2, 3, 6,7], 7)
    print(index)