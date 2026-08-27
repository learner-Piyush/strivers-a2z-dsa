"""
Title: Pattern 22
Topic: Patterns
Difficulty: Medium
Source: https://takeuforward.org/plus/dsa/problems/pattern-22?source=strivers-a2z-dsa-track
Date: 2026-08-27
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def pattern22(self, n):
        size = 2 * n - 1

        for i in range(size):
            for j in range(size):
                value = max(
                    abs(i - (n - 1)),
                    abs(j - (n - 1))
                ) + 1
                print(value, end=" ")
            print()


if __name__ == "__main__":
    n = int(input())
    Solution().pattern22(n)
