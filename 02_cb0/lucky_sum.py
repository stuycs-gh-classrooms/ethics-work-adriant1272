def lucky_sum(a, b, c):
  nums = [a,b,c]
  ret = 0
  for i in nums:
    if i==13:
      return ret
    ret += i
  return ret

print(lucky_sum(1, 2, 3)," → 6")
print(lucky_sum(1, 2, 13)," → 3")