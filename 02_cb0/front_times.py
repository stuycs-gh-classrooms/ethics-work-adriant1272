def front_times(str, n):
  i = 3
  if len(str) < n:
    i = len(str)
  return n*str[0:i]

print(front_times('Chocolate', 2)," → 'ChoCho'")
print(front_times('Chocolate', 3)," → 'ChoChoCho'")