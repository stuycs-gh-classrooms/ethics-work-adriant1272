def extra_end(str):
  return 3*str[len(str)-2:]

print(extra_end('Hello')," → 'lololo'")
print(extra_end('ab')," → 'ababab'")