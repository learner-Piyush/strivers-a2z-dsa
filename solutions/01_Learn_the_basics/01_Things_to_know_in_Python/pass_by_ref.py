"""
Title: Pass by Ref
Topic: Functions
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/pass-by-ref?source=strivers-a2z-dsa-track
Date: 2026-08-26
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def reverse(self, arr: list) -> None:
        left = 0
        right = len(arr) - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    Solution().reverse(arr)
    print(arr)
