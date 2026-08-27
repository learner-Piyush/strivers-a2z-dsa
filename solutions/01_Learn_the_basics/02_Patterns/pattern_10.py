"""
Title: Pattern 10
Topic: Patterns
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/pattern-10?source=strivers-a2z-dsa-track
Date: 2026-08-27
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def pattern10(self, n):
        # Increasing triangle
        for i in range(1, n + 1):
            print("*" * i)

        # Decreasing triangle
        for i in range(n - 1, 0, -1):
            print("*" * i)


if __name__ == "__main__":
    n = int(input())
    Solution().pattern10(n)
