"""
Title: Leaders in an Array
Topic: Arrays
Difficulty: Medium
Source: https://takeuforward.org/plus/dsa/problems/leaders-in-an-array?source=strivers-a2z-dsa-track
Date: 2026-09-05
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def leaders(self, nums):
        ans = []
        max_right = nums[-1]

        ans.append(max_right)

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > max_right:
                ans.append(nums[i])
                max_right = nums[i]

        return ans[::-1]


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().leaders(nums))
