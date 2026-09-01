"""
Title: Move Zeros to End
Topic: Arrays
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/move-zeros-to-end?source=strivers-a2z-dsa-track
Date: 2026-09-01
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def moveZeroes(self, nums):
        j = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    Solution().moveZeroes(nums)
    print(nums)
