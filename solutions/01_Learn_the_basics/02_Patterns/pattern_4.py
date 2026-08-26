"""
Title: Pattern 4
Topic: Patterns
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/pattern-4?source=strivers-a2z-dsa-track
Date: 2026-08-26
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def pattern4(self, n):
        for i in range(1, n + 1):
            print(str(i) * i)


if __name__ == "__main__":
    n = int(input())
    Solution().pattern4(n)
