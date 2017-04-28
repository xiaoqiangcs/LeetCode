class  LeetCode(object):
  """docstring for  LeetCode"""
  def _Quick_Sort(self, Array,left, Right):
    print(Array)
    if left>Right:
      return Array
    index=left
    for i in range(left+1, Right+1):
      if Array[i]<Array[left]:
        index+=1
        Array[index],Array[i]=Array[i],Array[index]
    Array[index],Array[left]=Array[left],Array[index]
    self._Quick_Sort(Array,left,index-1)
    self._Quick_Sort(Array,index+1,Right)
unsortedArray = [6, 5, 3, 1, 8, 7, 2, 4]
print(LeetCode()._Quick_Sort(unsortedArray, 0, len(unsortedArray) - 1))
