class Solution (object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        cutmini = [i-1 for i in range(len(s)+1)]
        for index in range(len(s)+1):
            for j in range(index):
                if s[j:index] == s[j:index][::-1]:
                    cutmini[index] = min(cutmini[index], 1+cutmini[j])
                else:
                    pass
        return cutmini[-1]
print(Solution().minCut("aab"))