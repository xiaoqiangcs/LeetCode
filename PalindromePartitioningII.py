class Solution (object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        cutmini = [i-1 for i in range(len(s)+1)]
        PaMatrix = self.getMat(s)
        for index in range(len(s)+1):
            for j in range(index):
                if PaMatrix[j][index-1]:
                    cutmini[index] = min(cutmini[index], 1+cutmini[j])
        return cutmini[-1]
    def getMat(self, s):
        PaMatrix=[[True for i in range(len(s))] for j in range(len(s))]
        for index in range(len(s),-1,-1):
             for j in range(index,len(s)):
                if index == j:
                    PaMatrix[index][j] = True
                else:
                    PaMatrix[index][j] = s[index]==s[j] and PaMatrix[index+1][j-1]
        return PaMatrix
print(Solution().minCut("aab"))