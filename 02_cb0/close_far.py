def close_far(a, b, c):
  return (abs(a-b) <=1 and abs(c-a) >=2 and abs(c-b) >=2) or (abs(a-c) <=1 and abs(b-a) >=2 and abs(c-b) >=2)

print(close_far(1, 2, 10)," → True")
print(close_far(1, 2, 3)," → False")