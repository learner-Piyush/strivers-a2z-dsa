"""
Title: Left Rotate Array by K Places
Topic: Arrays
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/left-rotate-array?source=strivers-a2z-dsa-track
Date: 2026-09-01
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def rotateArray(self, nums, k: int) -> None:
        n = len(nums)
        k %= n

        for i in range(k):
            first = nums[0]

            for j in range(1, n):
                nums[j - 1] = nums[j]

            nums[-1] = first


if __name__ == "__main__":
    k = int(input())
    nums = list(map(int, input().split()))
    Solution().rotateArray(nums, k)
    print(nums)
