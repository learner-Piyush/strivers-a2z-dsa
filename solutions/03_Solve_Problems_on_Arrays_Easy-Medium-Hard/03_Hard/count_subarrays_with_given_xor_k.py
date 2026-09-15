"""
Title: Count subarrays with given xor K
Topic: Arrays
Difficulty: Hard
Source: https://takeuforward.org/plus/dsa/problems/count-subarrays-with-given-xor-k?source=strivers-a2z-dsa-track
Date: 2026-09-15
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def subarraysWithXorK(self, nums, k):
        prefix_xor = 0
        count = 0

        # Frequency of prefix XORs
        freq = {0: 1}

        for num in nums:
            prefix_xor ^= num

            # We need a previous prefix XOR = prefix_xor ^ k
            required = prefix_xor ^ k

            count += freq.get(required, 0)

            # Store current prefix XOR
            freq[prefix_xor] = freq.get(prefix_xor, 0) + 1

        return count


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())

    print(Solution().subarraysWithXorK(nums, k))
