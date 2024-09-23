def last2(str):
  ret = 0
  if len(str) < 2:
    return ret
  last = str[-2:]
  c = 0
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last:
      c = c + 1

  return c

print(last2('xaxxaxaxx')," → 1")
print(last2('axxxaaxx')," → 2")