"""
Title: Pattern 20
Topic: Patterns
Difficulty: Medium
Source: https://takeuforward.org/plus/dsa/problems/pattern-20?source=strivers-a2z-dsa-track
Date: 2026-08-27
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def pattern20(self, n):
        # Upper half
        for i in range(1, n + 1):
            # Left stars
            for j in range(i):
                print("*", end="")

            # Spaces
            for j in range(2 * (n - i)):
                print(" ", end="")

            # Right stars
            for j in range(i):
                print("*", end="")

            print()

        # Lower half
        for i in range(n - 1, 0, -1):
            # Left stars
            for j in range(i):
                print("*", end="")

            # Spaces
            for j in range(2 * (n - i)):
                print(" ", end="")

            # Right stars
            for j in range(i):
                print("*", end="")

            print()


if __name__ == "__main__":
    n = int(input())
    Solution().pattern20(n)
