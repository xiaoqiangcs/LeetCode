'''
Problem Statement

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.
Example

For example, given the following matrix:
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
'''
class Soultion (object):
    def maximalSquare(self, matrix):
        if len(matrix) < 1 or not matrix:
            return 0
        result = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix[0])):
            result[0][i] = int(matrix[0][i])
        for j in range(len(matrix)):
            result[j][0]= int(matrix[j][0])
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if int(matrix[i][j]) == 1:
                    result[i][j] = min(result[i-1][j],result[i-1][j-1],result[i][j-1])+1
                    print(i,j)
                else:
                    result[i][j] = 0
        maxlength = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                maxlength = max(maxlength, result[i][j])
        return maxlength*maxlength
print(Soultion().maximalSquare(["10100","10111","11111","10010"]))