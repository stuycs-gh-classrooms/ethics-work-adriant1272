def centered_average(nums):
  bigs = nums[0]
  smalls = nums[0]
  ret = 0
  for i in nums:
    ret += i
    if i > bigs:
      bigs = i
    if i < smalls:
      smalls = i
  ret -= smalls
  ret -= abs(bigs)
  return ret / (len(nums)-2)

print(centered_average([1, 2, 3, 4, 100])," → 3")
print(centered_average([1, 1, 5, 5, 10, 8, 7])," → 5")