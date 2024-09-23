def make_chocolate(small, big, goal):
  if goal // 5 < big:
    wBig = goal //5
  else:
    wBig = big
  if goal-(wBig*5) <= small:
    return goal-(wBig*5)
  else:
    return -1


print(make_chocolate(4, 1, 9)," → 4")
print(make_chocolate(4, 1, 10)," → -1")
print(make_chocolate(4, 1, 7)," → 2")