def array123(nums):
  if len(nums) < 3:
    return False
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
      
  return False

print(array123([1, 1, 2, 3, 1])," → True")
print(array123([1, 1, 2, 4, 1])," → False")
