"""
Title: Recursive Bubble Sort
Topic: Array Sorting
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/recursive-bubble-sort?source=strivers-a2z-dsa-track
Date: 2026-08-29
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def bubbleSort(self, nums):
        def bubble(n):
            # Base case
            if n <= 1:
                return

            # One pass: move the largest element to the end
            for i in range(n - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]

            # Recursively sort the remaining part
            bubble(n - 1)

        bubble(len(nums))
        return nums


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().bubbleSort(nums))
