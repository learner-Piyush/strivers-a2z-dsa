"""
Title: Divisors of a Number
Topic: Basic Maths
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/divisors-of-a-number?source=strivers-a2z-dsa-track
Date: 2026-08-28
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def divisors(self, n):
        result = []

        i = 1
        while i * i <= n:
            if n % i == 0:
                result.append(i)

                if i != n // i:
                    result.append(n // i)

            i += 1

        result.sort()
        return result


if __name__ == "__main__":
    n = int(input())
    print(Solution().divisors(n))
