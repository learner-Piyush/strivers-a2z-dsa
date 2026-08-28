"""
Title: Check for Prime Number
Topic: Basic Maths
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/check-for-prime-number?source=strivers-a2z-dsa-track
Date: 2026-08-28
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def isPrime(self, n):
        #your code goes here
        if n <= 1:
            return False

        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1

        return True


if __name__ == "__main__":
    n = int(input())
    print(Solution().isPrime(n))
