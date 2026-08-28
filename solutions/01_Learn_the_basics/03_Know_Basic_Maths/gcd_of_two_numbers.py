"""
Title: GCD of Two Numbers
Topic: Basic Maths
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/gcd-of-two-numbers?source=strivers-a2z-dsa-track
Date: 2026-08-28
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def GCD(self, n1, n2):
        while n2 != 0:
            n1, n2 = n2, n1 % n2

        return n1


if __name__ == "__main__":
    n1 = int(input())
    n2 = int(input())
    print(Solution().GCD(n1, n2))
