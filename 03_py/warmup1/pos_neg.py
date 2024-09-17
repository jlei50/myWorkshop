def pos_neg(a, b, negative):
  if negative:
    return a * b > 0 and a < 0
  else:
    return a * b < 0
