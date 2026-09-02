"""
Title: Longest subarray with sum K
Topic: Arrays
Difficulty: Medium
Source: https://takeuforward.org/plus/dsa/problems/longest-subarray-with-sum-k?source=strivers-a2z-dsa-track
Date: 2026-09-02
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def longestSubarray(self, nums, k):
        prefix_sum = 0
        max_len = 0
        mp = {}

        for i in range(len(nums)):
            prefix_sum += nums[i]

            # If prefix_sum itself is k
            if prefix_sum == k:
                max_len = i + 1

            # We need an earlier prefix sum = prefix_sum - k
            if prefix_sum - k in mp:
                max_len = max(max_len, i - mp[prefix_sum - k])

            # Store only the first occurrence
            if prefix_sum not in mp:
                mp[prefix_sum] = i

        return max_len


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())
    print(Solution().longestSubarray(nums, k))
