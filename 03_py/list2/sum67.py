def sum67(nums):
  sum = 0
  ignore = False
  for i in nums:
    if i == 6:
      ignore = True
    elif i == 7 and ignore:
      ignore = False
      sum -= 7
    if (ignore == False):
      sum += i
      
  return sum