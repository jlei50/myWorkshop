def front_back(str):
  if len(str) > 1:
    return str[len(str)-1:] + str[1:len(str)-1] + str[0]
  else:
    return str