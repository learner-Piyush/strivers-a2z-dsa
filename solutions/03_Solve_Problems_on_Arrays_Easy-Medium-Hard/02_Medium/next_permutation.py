"""
Title: Next Permutation
Topic: Arrays
Difficulty: Medium
Source: https://takeuforward.org/plus/dsa/problems/next-permutation?source=strivers-a2z-dsa-track
Date: 2026-09-04
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def nextPermutation(self, nums):
        # Your code goes here
        n = len(nums)

        # 1. Find the first decreasing element from the right
        i = n - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 2. If a smaller element exists, find the next larger element
        if i >= 0:
            j = n - 1

            while nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        # 3. Reverse the part after i
        left = i + 1
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    Solution().nextPermutation(nums)
    print(nums)
