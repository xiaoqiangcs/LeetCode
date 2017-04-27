class Solution:
    # @param {int} n the nth
    # @return {string} the nth sequence
    def countAndSay(self, n):
        if n<=0:
            return ''
        if n==1:
            return '1'
        seq=self.countAndSay(n-1)
        result_seq=''
        index_seq=1
        for i in range(len(seq)):
          if i+1<len(seq) and seq[i]==seq[i+1]:
            index_seq+=1
          else:
            result_seq+=''+str(index_seq)
            result_seq+=''+str(seq[i])
            index_seq=1
        return result_seq
