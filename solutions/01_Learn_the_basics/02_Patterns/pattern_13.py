"""
Title: Pattern 13
Topic: Patterns
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/pattern-13?source=strivers-a2z-dsa-track
Date: 2026-08-27
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def pattern13(self, n):
        #your code goes here
        num = 1

        for i in range(1, n + 1):
            for j in range(i):
                print(num, end=" ")
                num += 1
            print()


if __name__ == "__main__":
    n = int(input())
    Solution().pattern13(n)
