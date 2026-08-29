"""
Title: Bubble Sort
Topic: Array Sorting
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/bubble-sort?source=strivers-a2z-dsa-track
Date: 2026-08-29
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def bubbleSort(self, nums):
        n = len(nums)

        for i in range(n):
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return nums


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().bubbleSort(nums))
