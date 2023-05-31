"""Traverse a list in reverse order."""
nums = [n for n in range(10)]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(nums)-1, -1, -1):
    print(nums[i])
