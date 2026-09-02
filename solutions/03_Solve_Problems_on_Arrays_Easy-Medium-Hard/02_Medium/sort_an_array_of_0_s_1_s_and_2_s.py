"""
Title: Sort an array of 0's 1's and 2's
Topic: Arrays
Difficulty: Medium
Source: https://takeuforward.org/plus/dsa/problems/sort-an-array-of-0's-1's-and-2's?source=strivers-a2z-dsa-track
Date: 2026-09-02
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def sortZeroOneTwo(self, nums):
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    Solution().sortZeroOneTwo(nums)
    print(nums)
