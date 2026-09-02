"""
Title: Single Number - I
Topic: Arrays
Difficulty: Medium
Source: https://takeuforward.org/plus/dsa/problems/single-number---i?source=strivers-a2z-dsa-track
Date: 2026-09-02
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def singleNumber(self, nums):
        #your code goes here
        result = 0

        for num in nums:
            result ^= num

        return result


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().singleNumber(nums))
