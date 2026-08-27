"""
Title: Pattern 19
Topic: Patterns
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/pattern-19?source=strivers-a2z-dsa-track
Date: 2026-08-27
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def pattern19(self, n):
        # Upper half
        for i in range(n):
            # Left stars
            for j in range(n - i):
                print("*", end="")

            # Spaces
            for j in range(2 * i):
                print(" ", end="")

            # Right stars
            for j in range(n - i):
                print("*", end="")

            print()

        # Lower half
        for i in range(n):
            # Left stars
            for j in range(i + 1):
                print("*", end="")

            # Spaces
            for j in range(2 * (n - i - 1)):
                print(" ", end="")

            # Right stars
            for j in range(i + 1):
                print("*", end="")

            print()


if __name__ == "__main__":
    n = int(input())
    Solution().pattern19(n)
