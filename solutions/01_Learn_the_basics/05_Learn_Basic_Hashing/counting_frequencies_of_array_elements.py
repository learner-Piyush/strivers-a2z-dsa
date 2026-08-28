"""
Title: Counting Frequencies of Array Elements
Topic: Hashing
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/counting-frequencies-of-array-elements?source=strivers-a2z-dsa-track
Date: 2026-08-28
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def countFrequencies(self, nums):
        # Your code goes here
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        return [[num, count] for num, count in freq.items()]



if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().countFrequencies(nums))
