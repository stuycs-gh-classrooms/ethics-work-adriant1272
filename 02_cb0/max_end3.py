def max_end3(nums):
 if nums[0] > nums[2]:
   return [nums[0], nums[0], nums[0]]
 else:
   return [nums[2], nums[2], nums[2]]

print(max_end3([1, 2, 3])) 
print("...should return [3, 3, 3]")

print(max_end3([11, 5, 9]))
print("...return [11, 11, 11]")

print(max_end3([2, 11, 3]))
print("...should return [3, 3, 3]")
