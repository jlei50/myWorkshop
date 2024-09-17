def front_times(str, n):
  if len(str) > 3:
    front = str[:3]
  else:
    front = str
  return front * n