def rotate_left3(nums):
  temp = nums[0]
  for i in range(len(nums) -1):
    nums[i] = nums[i+1]
  nums[-1] = temp
  return nums
