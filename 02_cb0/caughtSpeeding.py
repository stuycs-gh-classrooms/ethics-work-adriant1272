def caught_speeding(speed, is_birthday):
  if not is_birthday:
    rate = speed
  else:
    rate = speed - 5
    
  if rate<=60: return 0
  if rate>=61 and rate<=80: return 1
  if rate>=81: return 2
  
