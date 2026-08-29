"""
Title: Quick Sorting
Topic: Array Sorting
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/quick-sorting?source=strivers-a2z-dsa-track
Date: 2026-08-29
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def quickSort(self, nums):
        def partition(low, high):
            pivot = nums[high]
            i = low - 1

            for j in range(low, high):
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]

            nums[i + 1], nums[high] = nums[high], nums[i + 1]
            return i + 1

        def quick(low, high):
            if low < high:
                pivot_index = partition(low, high)

                quick(low, pivot_index - 1)
                quick(pivot_index + 1, high)

        quick(0, len(nums) - 1)

        return nums


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().quickSort(nums))
