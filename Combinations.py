class Solution(object):
    """
    Problem Statement

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
Example

For example, If n = 4 and k = 2, a solution is: [[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]]
    """
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n<k:
            return None
        res=[]
        self.helper(n,1,k,res,[])
        return res
        
    def helper(self,n,pos,k,res,temp):
        if len(temp)==k:
            res.append([]+temp)
            return
        for pos in range(pos,n+1):
            temp.append(pos)
            self.helper(n,pos+1,k,res,temp)
            temp.pop()

if __name__ == '__main__':
    index = Solution().combine(4,2)
    print(index)