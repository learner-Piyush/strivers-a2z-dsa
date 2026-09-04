"""
Title: Kadane's Algorithm
Topic: Arrays
Difficulty: Medium
Source: https://takeuforward.org/plus/dsa/problems/kadane's-algorithm?source=strivers-a2z-dsa-track
Date: 2026-09-04
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def maxSubArray(self, nums):
        current = nums[0]
        maximum = nums[0]

        for num in nums[1:]:
            current = max(num, current + num)
            maximum = max(maximum, current)

        return maximum


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().maxSubArray(nums))
