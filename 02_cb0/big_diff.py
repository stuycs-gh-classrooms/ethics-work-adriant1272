def big_diff(nums):
  bigs = nums[0]
  smalls = nums[0]
  for i in nums:
    if i > bigs:
      bigs = i
    if i < smalls:
      smalls = i
  return abs(bigs-smalls)

print(big_diff([7, 2, 10, 9])," → 8")
print(big_diff([2, 10, 7, 2])," → 8")