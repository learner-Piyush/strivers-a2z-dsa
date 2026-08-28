"""
Title: Check if the Number is Armstrong
Topic: Basic Maths
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/check-if-the-number-if-armstrong?source=strivers-a2z-dsa-track
Date: 2026-08-28
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def isArmstrong(self, n):
        original = n
        digits = len(str(n))
        total = 0

        while n > 0:
            digit = n % 10
            total += digit ** digits
            n //= 10

        return total == original


if __name__ == "__main__":
    n = int(input())
    print(Solution().isArmstrong(n))
