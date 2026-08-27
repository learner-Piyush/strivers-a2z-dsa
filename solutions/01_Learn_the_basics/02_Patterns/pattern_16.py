"""
Title: Pattern 16
Topic: Patterns
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/pattern-16?source=strivers-a2z-dsa-track
Date: 2026-08-27
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def pattern16(self, n):
        for i in range(n):
            for j in range(i + 1):
                print(chr(65 + i), end="")
            print()


if __name__ == "__main__":
    n = int(input())
    Solution().pattern16(n)
