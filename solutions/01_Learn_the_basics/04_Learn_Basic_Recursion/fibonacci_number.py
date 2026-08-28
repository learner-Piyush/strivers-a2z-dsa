"""
Title: Fibonacci Number
Topic: Recursion
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/fibonacci-number?source=strivers-a2z-dsa-track
Date: 2026-08-28
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def fib(self, n):
        #your code goes here
        if n == 0:
            return 0

        if n == 1:
            return 1

        return self.fib(n - 1) + self.fib(n - 2)


if __name__ == "__main__":
    n = int(input())
    print(Solution().fib(n))
