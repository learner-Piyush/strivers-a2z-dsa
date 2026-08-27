"""
Title: Pattern 15
Topic: Patterns
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/pattern-15?source=strivers-a2z-dsa-track
Date: 2026-08-27
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def pattern15(self, n):
        for i in range(n, 0, -1):
            for j in range(i):
                print(chr(65 + j), end="")
            print()


if __name__ == "__main__":
    n = int(input())
    Solution().pattern15(n)
