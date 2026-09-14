"""
Title: Count subarrays with given sum
Topic: Arrays
Difficulty: Medium
Source: https://takeuforward.org/plus/dsa/problems/count-subarrays-with-given-sum?source=strivers-a2z-dsa-track
Date: 2026-09-14
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def subarraySum(self, nums, k):
        prefix_count = {0: 1}
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num

            # If current_sum - k exists, those subarrays sum to k
            count += prefix_count.get(current_sum - k, 0)

            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

        return count


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())
    print(Solution().subarraySum(nums, k))
