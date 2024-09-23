def count_evens(nums):
  ret = 0
  for i in nums:
    if i%2==0:
      ret+=1
  return ret