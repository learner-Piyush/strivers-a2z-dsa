"""
Title: Remove duplicates from sorted array
Topic: Arrays
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/remove-duplicates-from-sorted-array?source=strivers-a2z-dsa-track
Date: 2026-08-31
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().removeDuplicates(nums))
