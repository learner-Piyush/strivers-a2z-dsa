"""
Title: Selection Sort
Topic: Array Sorting
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/selection-sort?source=strivers-a2z-dsa-track
Date: 2026-08-29
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def selectionSort(self, nums):
        n = len(nums)

        for i in range(n):
            min_idx = i

            for j in range(i + 1, n):
                if nums[j] < nums[min_idx]:
                    min_idx = j

            nums[i], nums[min_idx] = nums[min_idx], nums[i]

        return nums


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().selectionSort(nums))
