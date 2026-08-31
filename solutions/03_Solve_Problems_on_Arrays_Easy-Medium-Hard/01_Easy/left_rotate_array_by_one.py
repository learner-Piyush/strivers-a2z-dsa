"""
Title: Left Rotate Array by One
Topic: Arrays
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/left-rotate-array-by-one?source=strivers-a2z-dsa-track
Date: 2026-08-31
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def rotateArrayByOne(self, nums):
        first = nums[0]

        for i in range(1, len(nums)):
            nums[i - 1] = nums[i]

        nums[-1] = first


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    Solution().rotateArrayByOne(nums)
    print(nums)
