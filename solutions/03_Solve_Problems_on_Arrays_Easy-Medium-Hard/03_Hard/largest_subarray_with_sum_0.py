"""
Title: Largest Subarray with Sum 0
Topic: Arrays
Difficulty: Medium
Source: https://takeuforward.org/plus/dsa/problems/largest-subarray-with-sum-0?source=strivers-a2z-dsa-track
Date: 2026-09-15
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def maxLen(self, arr):
        # Your code goes here
        prefix_sum = 0
        max_length = 0
        first_index = {0: -1}

        for i, num in enumerate(arr):
            prefix_sum += num

            if prefix_sum in first_index:
                max_length = max(max_length, i - first_index[prefix_sum])
            else:
                first_index[prefix_sum] = i

        return max_length


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(Solution().maxLen(arr))
