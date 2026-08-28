"""
Title: Sum of First N Numbers
Topic: Recursion
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/sum-of-first-n-numbers?source=strivers-a2z-dsa-track
Date: 2026-08-28
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def NnumbersSum(self, N):
        #your code goes here
        if N == 0:
            return 0

        return N + self.NnumbersSum(N - 1)


if __name__ == "__main__":
    n = int(input())
    print(Solution().NnumbersSum(n))
