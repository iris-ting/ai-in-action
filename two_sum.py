# LeetCode Two Sum: Given an integer array nums and an integer target,
# return the indices of the two numbers such that they add up to target.
def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]
        lookup[num] = i