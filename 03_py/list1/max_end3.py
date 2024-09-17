def max_end3(nums):
  for i in range(len(nums)):
    nums[i] = max(nums[0], nums[-1])
    
  return nums
