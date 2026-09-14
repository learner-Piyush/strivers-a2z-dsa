"""
Title: Pascal's Triangle I
Topic: Arrays
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/pascals-triangle-i?source=strivers-a2z-dsa-track
Date: 2026-09-14
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def pascalTriangleI(self, r, c):
        # Value at row r, column c = C(r-1, c-1)
        n = r - 1
        k = c - 1

        result = 1

        for i in range(k):
            result = result * (n - i) // (i + 1)

        return result


if __name__ == "__main__":
    r = int(input())
    c = int(input())
    print(Solution().pascalTriangleI(r, c))
