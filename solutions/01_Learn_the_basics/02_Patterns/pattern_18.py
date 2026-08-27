"""
Title: Pattern 18
Topic: Patterns
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/pattern-18?source=strivers-a2z-dsa-track
Date: 2026-08-27
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def pattern18(self, n):
        for i in range(n):
            for j in range(n - i - 1, n):
                print(chr(65 + j), end=" ")
            print()


if __name__ == "__main__":
    n = int(input())
    Solution().pattern18(n)
