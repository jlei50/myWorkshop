def string_match(a, b):
  num = 0
  for chrs in range(len(a) - 1):
    ch = a[chrs:chrs+2]
    for chrs2 in range(len(b) - 1):
      if ch == b[chrs2:chrs+2]:
        num += 1
        
  return num
