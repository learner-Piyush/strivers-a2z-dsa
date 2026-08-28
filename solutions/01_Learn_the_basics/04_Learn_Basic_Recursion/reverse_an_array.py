"""
Title: Reverse an array
Topic: Recursion
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/reverse-an-array?source=strivers-a2z-dsa-track
Date: 2026-08-28
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def reverse(self, arr: list, n: int) -> None:
        def reverse_array(left, right):
            if left >= right:
                return

            arr[left], arr[right] = arr[right], arr[left]
            reverse_array(left + 1, right - 1)

        reverse_array(0, n - 1)



if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    Solution().reverse(arr, n)
    print(arr)
