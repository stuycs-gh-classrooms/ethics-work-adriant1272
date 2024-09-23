def sum67(nums):
  ct = True
  ret = 0
  for i in nums:
    if i==6:
      ct = False
    if ct:
      ret += i
    if i==7:
      ct = True
  return ret