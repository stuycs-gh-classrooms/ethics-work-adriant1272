def string_match(a, b):
  ret = 0
  for i in range(len(a)-1):
    if a[i:i+2] == b[i:i+2]:
      ret += 1
  return ret

print(string_match('xxcaazz', 'xxbaaz')," → 3")
print(string_match('abc', 'abc')," → 2")