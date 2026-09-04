"""
Title: Majority Element-I
Topic: Arrays
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/majority-element-i?source=strivers-a2z-dsa-track
Date: 2026-09-04
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def majorityElement(self, nums):
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().majorityElement(nums))
