"""
Title: Print N to 1 using Recursion
Topic: Recursion
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/print-n-to-1-using-recursion?source=strivers-a2z-dsa-track
Date: 2026-08-28
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def printNumbers(self, n):
        # Your code goes here
        if n == 0:
            return

        print(n)
        self.printNumbers(n - 1)


if __name__ == "__main__":
    n = int(input())
    Solution().printNumbers(n)
