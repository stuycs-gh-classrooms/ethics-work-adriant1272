def array_count9(nums):
  ret = 0
  for i in nums:
    if i==9:
      ret += 1
  return ret

print(array_count9([1, 2, 9])," → 1")
print(array_count9([1, 9, 9])," → 2")