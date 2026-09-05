"""
Title: Rotate matrix by 90 degrees
Topic: Arrays
Difficulty: Medium
Source: https://takeuforward.org/plus/dsa/problems/rotate-matrix-by-90-degrees?source=strivers-a2z-dsa-track
Date: 2026-09-05
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def rotateMatrix(self, matrix):
        n = len(matrix)

        # Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse every row
        for i in range(n):
            matrix[i].reverse()


if __name__ == "__main__":
    n = int(input())

    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    Solution().rotateMatrix(matrix)

    for row in matrix:
        print(*row)
