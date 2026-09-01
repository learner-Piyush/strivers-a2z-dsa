"""
Title: Find missing number
Topic: Arrays
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/find-missing-number?source=strivers-a2z-dsa-track
Date: 2026-09-01
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        expected = n * (n + 1) // 2

        return expected - sum(nums)


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().missingNumber(nums))
