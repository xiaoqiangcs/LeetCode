class Soultion (object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)
        if len3!=len1+len2:
            return False
        result=[[True for i in range(1+len2)] for j in range(1+len1)]
        for i1 in range(1, 1+len1):
            if s1[i1-1] == s3[i1-1] and result[i1-1][0]:
                result[i1][0] = True
            else:
                result[i1][0] = False
        for i2 in range(1, 1+len2):
            if s2[i2-1] == s3[i2-1] and result[0][i2-1]:
                result[0][i2] = True
            else:
                result[0][i2] = False
        for i1 in range(1, len1+1):
            for i2 in range(1, len2+1):
                case1 = s1[i1-1] == s3[i1+i2-1] and result[i1-1][i2]
                case2 = s2[i2-1] == s3[i1+i2-1] and result[i1][i2-1]
                result[i1][i2] = case1 or case2
        return result[len1][len2]

print(Soultion().isInterleave("aabcc","dbbca", "aadbbbaccc"))
