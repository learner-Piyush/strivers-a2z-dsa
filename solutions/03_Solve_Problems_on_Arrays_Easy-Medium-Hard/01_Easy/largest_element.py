"""
Title: Largest Element
Topic: Arrays
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/largest-element?source=strivers-a2z-dsa-track
Date: 2026-08-31
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def largestElement(self, nums):
        largest = nums[0]

        for num in nums:
            if num > largest:
                largest = num

        return largest


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().largestElement(nums))
