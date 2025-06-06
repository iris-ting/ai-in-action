# LeetCode Two Sum 解法：給定一個整數陣列 nums 和一個目標值 target，
# 請你回傳兩個數字的 index，其總和等於 target。

def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]
        lookup[num] = i