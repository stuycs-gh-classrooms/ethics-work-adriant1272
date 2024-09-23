def front_back(str):
  if len(str)<=1: return str
  
  
  front = str[0]
  middle = str[1:-1]
  back = str[-1]
  return back + middle + front

print(front_back('a'))