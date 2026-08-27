"""
Title: Reverse a number
Topic: Basic Maths
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/reverse-a-number?source=strivers-a2z-dsa-track
Date: 2026-08-27
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def reverseNumber(self, n):
        reverse = 0

        while n > 0:
            digit = n % 10
            reverse = reverse * 10 + digit
            n //= 10

        return reverse


if __name__ == "__main__":
    n = int(input())
    print(Solution().reverseNumber(n))
