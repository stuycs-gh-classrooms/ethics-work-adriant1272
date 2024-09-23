def sum13(nums):
  gd = True
  ret = 0
  for i in range(len(nums)):
    if nums[i]==13:
      gd=False
    else:
      if gd:
        ret += nums[i]
      gd = True
  return ret

print(sum13([1, 2, 2, 1])," → 6")
print(sum13([1, 1])," → 2")