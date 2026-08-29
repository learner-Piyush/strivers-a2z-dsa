"""
Title: Merge Sorting
Topic: Array Sorting
Difficulty: Medium
Source: https://takeuforward.org/plus/dsa/problems/merge-sorting?source=strivers-a2z-dsa-track
Date: 2026-08-29
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])

        result = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().mergeSort(nums))
