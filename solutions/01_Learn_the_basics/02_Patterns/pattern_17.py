"""
Title: Pattern 17
Topic: Patterns
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/pattern-17?source=strivers-a2z-dsa-track
Date: 2026-08-27
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def pattern17(self, n):
        for i in range(1, n + 1):
            # Spaces
            for j in range(n - i):
                print(" ", end="")

            # Increasing letters
            for j in range(1, i + 1):
                print(chr(64 + j), end="")

            # Decreasing letters
            for j in range(i - 1, 0, -1):
                print(chr(64 + j), end="")

            print()


if __name__ == "__main__":
    n = int(input())
    Solution().pattern17(n)
