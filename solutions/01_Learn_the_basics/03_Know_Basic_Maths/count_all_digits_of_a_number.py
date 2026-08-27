"""
Title: Count all Digits of a Number
Topic: Basic Maths
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/count-all-digits-of-a-number?source=strivers-a2z-dsa-track
Date: 2026-08-27
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def countDigit(self, n):
        if n == 0:
            return 1

        count = 0

        while n > 0:
            n //= 10
            count += 1

        return count


if __name__ == "__main__":
    n = int(input())
    print(Solution().countDigit(n))
