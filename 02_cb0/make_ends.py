def make_ends(nums):
  return [nums[0], nums[len(nums)-1]]

print(make_ends([1, 2, 3]))
print("...should be [1,3]")

print(make_ends([1, 2, 3, 4]))
print("...should be [1, 4]")

print(make_ends([7, 4, 6, 2]))
print("...should be [7,2]")
