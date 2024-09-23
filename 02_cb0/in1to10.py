def in1to10(n, outside_mode):
  if n==9 and outside_mode==True:
    return False
  in_range = n>=1 and n<=10
  return (outside_mode and not (in_range)) or ( in_range)