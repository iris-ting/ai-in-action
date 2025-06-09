# LeetCode 121: Best Time to Buy and Sell Stock
# Given an array prices where prices[i] is the price of a given stock on the ith day,
# return the maximum profit you can achieve from a single buy and sell.
# You must buy before you sell.

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        # update the minimum price seen so far
        min_price = min(min_price, price)
        # update the maximum profit so far
        max_profit = max(max_profit, price - min_price)

    return max_profit