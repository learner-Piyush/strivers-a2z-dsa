"""
Title: Merge Overlapping Subintervals
Topic: Arrays
Difficulty: Medium
Source: https://takeuforward.org/plus/dsa/problems/merge-overlapping-subintervals?source=strivers-a2z-dsa-track
Date: 2026-09-15
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def mergeOverlap(self, intervals):
        # Your code goes here
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])

        return merged


if __name__ == "__main__":
    n = int(input())
    intervals = []

    for i in range(n):
        start, end = map(int, input().split())
        intervals.append([start, end])

    print(Solution().mergeOverlap(intervals))
