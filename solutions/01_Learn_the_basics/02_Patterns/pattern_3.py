"""
Title: Pattern 3
Topic: Patterns
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/pattern-3?source=strivers-a2z-dsa-track
Date: 2026-08-26
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def pattern3(self, n):
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end="")
            print()


if __name__ == "__main__":
    n = int(input())
    Solution().pattern3(n)
