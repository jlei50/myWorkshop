def reverse3(nums):
  nums2 = []
  for i in range(len(nums)):
    nums2.append(nums[len(nums) - 1 - i])
  return nums2