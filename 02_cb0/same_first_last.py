def same_first_last(nums):
   if len(nums) < 1:
     return False;
   elif nums[0] == nums[len(nums) - 1]:
     return True;
   else:
     return False;

print(same_first_last([1,2,3]))
print("...should be False")

print(same_first_last([1,2,3,1]))
print("...should be True")

print(same_first_last([1,2,1]))
print("...should be True")
