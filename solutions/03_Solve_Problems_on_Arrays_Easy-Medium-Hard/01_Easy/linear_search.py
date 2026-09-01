"""
Title: Linear Search
Topic: Arrays
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/linear-search?source=strivers-a2z-dsa-track
Date: 2026-09-01
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def linearSearch(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i

        return -1


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    x = int(input())
    print(Solution().linearSearch(nums, x))
