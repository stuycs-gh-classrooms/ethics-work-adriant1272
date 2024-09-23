def string_splosion(str):
  ret =""
  for i in range(len(str)):
    ret+= str[0:i+1]
    
  return ret

print(string_splosion('Code')," → 'CCoCodCode'")
print(string_splosion('abc')," → 'aababc'")
print(string_splosion('ab')," → 'aab'")