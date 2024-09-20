def pos_neg(a, b, negative):
  if (a<0 or b<0) and not (a<0 and b<0) and not negative: return True
  if (a<0 and b<0) and negative: return True
  else: return False
