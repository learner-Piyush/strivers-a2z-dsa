"""
Title: While Loops
Topic: Basics
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/while-loop?source=strivers-a2z-dsa-track
Date: 2026-08-26
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def whileLoop(self, d : int) -> int:
        # Your code goes here
        count = 0
        num = d
        total = 0

        if d == 0:
            num = 10

        while count < 50:
            total += num
            count += 1
            num += 10

        return total


if __name__ == "__main__":
    d = int(input())
    print(Solution().whileLoop(d))
