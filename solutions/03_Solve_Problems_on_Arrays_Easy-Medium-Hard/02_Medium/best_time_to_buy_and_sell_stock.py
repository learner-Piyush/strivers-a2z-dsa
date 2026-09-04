"""
Title: Best time to buy and sell stock
Topic: Arrays
Difficulty: Medium
Source: https://takeuforward.org/plus/dsa/problems/best-time-to-buy-and-sell-stock?source=strivers-a2z-dsa-track
Date: 2026-09-04
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def stockBuySell(self, arr, n):
        min_price = arr[0]
        max_profit = 0

        for price in arr[1:]:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().stockBuySell(nums, len(nums)))
