"""
Title: Pattern 21
Topic: Patterns
Difficulty: Medium
Source: https://takeuforward.org/plus/dsa/problems/pattern-21?source=strivers-a2z-dsa-track
Date: 2026-08-27
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def pattern21(self, n):
        for i in range(n):
            for j in range(n):
                if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()


if __name__ == "__main__":
    n = int(input())
    Solution().pattern21(n)
