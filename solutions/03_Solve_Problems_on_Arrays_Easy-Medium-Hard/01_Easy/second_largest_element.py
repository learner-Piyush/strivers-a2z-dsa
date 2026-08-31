"""
Title: Second Largest Element
Topic: Arrays
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/second-largest-element?source=strivers-a2z-dsa-track
Date: 2026-08-31
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def secondLargestElement(self, nums):
        largest = nums[0]
        second_largest = None

        for num in nums:
            if num > largest:
                second_largest = largest
                largest = num
            elif num != largest and (second_largest is None or num > second_largest):
                second_largest = num

        if second_largest is None:
            return -1

        return second_largest


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().secondLargestElement(nums))
