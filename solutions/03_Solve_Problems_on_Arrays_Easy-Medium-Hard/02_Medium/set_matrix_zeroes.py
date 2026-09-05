"""
Title: Set Matrix Zeroes
Topic: Arrays
Difficulty: Medium
Source: https://takeuforward.org/plus/dsa/problems/set-matrix-zeroes?source=strivers-a2z-dsa-track
Date: 2026-09-05
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def setZeroes(self, matrix):
        # Your code goes here
        m = len(matrix)
        n = len(matrix[0])

        first_row = False
        first_col = False

        # Check if first row contains 0
        for j in range(n):
            if matrix[0][j] == 0:
                first_row = True

        # Check if first column contains 0
        for i in range(m):
            if matrix[i][0] == 0:
                first_col = True

        # Use first row and first column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set marked rows to 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        # Set marked columns to 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        # Handle first row
        if first_row:
            for j in range(n):
                matrix[0][j] = 0

        # Handle first column
        if first_col:
            for i in range(m):
                matrix[i][0] = 0


if __name__ == "__main__":
    m, n = map(int, input().split())

    matrix = []
    for i in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)

    Solution().setZeroes(matrix)

    for row in matrix:
        print(*row)
