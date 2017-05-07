class Solution (object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return True
        if not wordDict:
            return False
        max_word_len = max([len(index) for index in wordDict])
        result = [False for i in range(len(s)+1)]
        result[0] = True
        for index_s in range(len(s)):
            for j in range(index_s, -1, -1):
                if index_s-j+1 > max_word_len:
                    break
                if result[j] and s[j:index_s+1] in wordDict:
                    result[index_s+1] = True
                    break
        return (result[-1])
print(Solution().wordBreak("leetcode", ["leet", "code"]))