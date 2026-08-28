"""
Title: Factorial of a given number
Topic: Recursion
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/factorial-of-a-given-number-i?source=strivers-a2z-dsa-track
Date: 2026-08-28
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1

        return n * self.factorial(n - 1)


if __name__ == "__main__":
    n = int(input())
    print(Solution().factorial(n))
