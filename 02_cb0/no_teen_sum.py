def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)
  
def fix_teen(n):
  if n==15 or n==16 or n < 13 or n > 19:
    return n
  return 0

print(no_teen_sum(1, 2, 3)," → 6")
print(no_teen_sum(2, 13, 1)," → 3")