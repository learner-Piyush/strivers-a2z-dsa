"""
Title: 3 Sum
Topic: Arrays
Difficulty: Medium
Source: https://takeuforward.org/plus/dsa/problems/3-sum?source=strivers-a2z-dsa-track
Date: 2026-09-14
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def threeSum(self, nums: list) -> list[list]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate pairs
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().threeSum(nums))
