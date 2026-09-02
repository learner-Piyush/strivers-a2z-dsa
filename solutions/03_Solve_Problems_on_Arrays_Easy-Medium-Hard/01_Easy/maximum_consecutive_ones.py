"""
Title: Maximum Consecutive Ones
Topic: Arrays
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/maximum-consecutive-ones?source=strivers-a2z-dsa-track
Date: 2026-09-02
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        max_count = 0

        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0

        return max_count


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().findMaxConsecutiveOnes(nums))
