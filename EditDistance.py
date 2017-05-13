class Soultion (object):
    def minDistance(self, word1, word2):
        len1 = len(word1)
        len2 = len(word2)
        if not word1 or not word2:
            return max(len1, len2)
        distance = [[i+j for i in range(1+len2)] for j in range(1+len1)]
        for index_1 in range(1, len1+1):
            for index_2 in range(1, 1+len2):
                if word1[index_1-1] == word2[index_2-1]:
                    distance[index_1][index_2] = min(distance[index_1-1][index_2-1], 1+distance[index_1-1][index_2], 1+distance[index_1][index_2-1])
                else:
                    distance[index_1][index_2] = 1+min(distance[index_1-1][index_2-1], distance[index_1-1][index_2], distance[index_1][index_2-1])
        return distance[index_1][index_2]
print(Soultion().minDistance("mart","karma"))