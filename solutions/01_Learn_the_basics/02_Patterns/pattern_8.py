"""
Title: Pattern 8
Topic: Patterns
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/pattern-8?source=strivers-a2z-dsa-track
Date: 2026-08-26
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def pattern8(self, n):
        for i in range(n, 0, -1):
            spaces = n - i
            stars = 2 * i - 1
            print(" " * spaces + "*" * stars)


if __name__ == "__main__":
    n = int(input())
    Solution().pattern8(n)
