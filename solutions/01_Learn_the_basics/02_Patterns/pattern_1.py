"""
Title: Pattern 1
Topic: Patterns
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/pattern-1?source=strivers-a2z-dsa-track
Date: 2026-08-26
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def pattern1(self, n):
        for i in range(n):
            print("*" * n)


if __name__ == "__main__":
    n = int(input())
    Solution().pattern1(n)
