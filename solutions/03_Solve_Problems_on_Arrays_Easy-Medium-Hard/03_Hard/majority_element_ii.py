"""
Title: Majority Element-II
Topic: Arrays
Difficulty: Hard
Source: https://takeuforward.org/plus/dsa/problems/majority-element-ii?source=strivers-a2z-dsa-track
Date: 2026-09-14
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def majorityElementTwo(self, nums):
        n = len(nums)

        count1 = count2 = 0
        candidate1 = candidate2 = None

        # Boyer-Moore Voting Algorithm
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        # Verify the candidates
        count1 = count2 = 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        result = []

        if count1 > n // 3:
            result.append(candidate1)

        if count2 > n // 3:
            result.append(candidate2)

        return result


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().majorityElementTwo(nums))
