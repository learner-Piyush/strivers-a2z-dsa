"""
Title: Two Sum
Topic: Arrays
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/two-sum?source=strivers-a2z-dsa-track
Date: 2026-09-02
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def twoSum(self, nums, target):
        mp = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in mp:
                return [mp[complement], i]

            mp[nums[i]] = i


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    x = int(input())
    print(Solution().twoSum(nums, x))
