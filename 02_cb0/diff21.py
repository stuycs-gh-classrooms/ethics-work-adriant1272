def diff21(n):
  if n > 21:
    return 2*abs(21-n)
  else:
    return abs(21-n)

print(diff21(19)" → 2")
print(diff21(10)" → 11")
print(diff21(21)" → 0")
