"""
Title: Check if the Array is Sorted II
Topic: Arrays
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/check-if-the-array-is-sorted-ii?source=strivers-a2z-dsa-track
Date: 2026-08-31
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def isSorted(self, nums):
        #your code goes here
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return False

        return True


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().isSorted(nums))
