def lone_sum(a, b, c):
  ret = 0
  if a!= c and a!=b:
    ret += a
  if b!= c and a!=b:
    ret += b
  if a!= c and c!=b:
    ret += c
  return ret

print(lone_sum(1, 2, 3)," → 6")
print(lone_sum(3, 2, 3)," → 2")