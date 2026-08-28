"""
Title: Highest Occurring Element in an Array
Topic: Hashing
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/highest-occurring-element-in-an-array?source=strivers-a2z-dsa-track
Date: 2026-08-28
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def mostFrequentElement(self, nums):
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        ans = nums[0]

        for num in freq:
            if freq[num] > freq[ans]:
                ans = num
            elif freq[num] == freq[ans] and num < ans:
                ans = num

        return ans
     


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().mostFrequentElement(nums))
