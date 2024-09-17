def last2(str):
  num = 0
  last = str[len(str)-2:]
  for i in range(len(str)-2):
    if str[i:i+2] == last:
      num+=1
  return num
