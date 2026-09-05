"""
Title: Longest Consecutive Sequence in an Array
Topic: Arrays
Difficulty: Medium
Source: https://takeuforward.org/plus/dsa/problems/longest-consecutive-sequence-in-an-array?source=strivers-a2z-dsa-track
Date: 2026-09-05
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                current = num
                count = 1

                while current + 1 in num_set:
                    current += 1
                    count += 1

                longest = max(longest, count)

        return longest


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().longestConsecutive(nums))
