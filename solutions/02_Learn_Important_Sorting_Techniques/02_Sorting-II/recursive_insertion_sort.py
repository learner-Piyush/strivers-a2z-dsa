"""
Title: Recursive Insertion Sort
Topic: Array Sorting
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/recursive-insertion-sort?source=strivers-a2z-dsa-track
Date: 2026-08-29
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def insertionSort(self, nums):
        def insert(i):
            # Base case
            if i == 0:
                return

            # Sort the previous elements first
            insert(i - 1)

            # Insert nums[i] into the sorted portion
            key = nums[i]
            j = i - 1

            def shift(j):
                if j < 0 or nums[j] <= key:
                    nums[j + 1] = key
                    return

                nums[j + 1] = nums[j]
                shift(j - 1)

            shift(j)
        
        insert(len(nums) - 1)
        return nums


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().insertionSort(nums))
