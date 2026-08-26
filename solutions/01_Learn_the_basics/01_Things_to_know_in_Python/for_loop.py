"""
Title: For Loops
Topic: Basics
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/for-loop?source=strivers-a2z-dsa-track
Date: 2026-08-26
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def forLoop(self, low : int, high : int) -> int:
        # Your code goes here
        total = 0
        for i in range(low, high + 1):
            total += i
        return total


if __name__ == "__main__":
    low = int(input())
    high = int(input())
    print(Solution().forLoop(low, high))
