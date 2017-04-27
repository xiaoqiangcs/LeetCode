class RotatedArray(object):
  """docstring for RotatedArray"""
  def  searchArray(self, nums, target):
    left=0
    right=len(nums)-1
    while left<=right:
      mid=left+(right-left)/2
      if target==nums[mid]:
        return mid
      elif nums[left]<nums[mid]:
        if target>=nums[left] and target<=nums[mid]:
          right=mid-1
        else :
          left=mid+1
      elif nums[left]>nums[mid]:
        if target>=nums[mid] and target<=nums[right]:
          left=mid+1
        else :
          right=mid-1
      else:
        left+=1
    return -1

Test=RotatedArray()
print (Test.searchArray([4,5,6,7,0,1,2],2))
