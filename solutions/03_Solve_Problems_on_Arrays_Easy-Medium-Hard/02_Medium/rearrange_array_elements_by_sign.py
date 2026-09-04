"""
Title: Rearrange array elements by sign
Topic: Arrays
Difficulty: Medium
Source: https://takeuforward.org/plus/dsa/problems/rearrange-array-elements-by-sign?source=strivers-a2z-dsa-track
Date: 2026-09-04
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def rearrangeArray(self, nums):
        ans = [0] * len(nums)

        pos = 0
        neg = 1

        for num in nums:
            if num > 0:
                ans[pos] = num
                pos += 2
            else:
                ans[neg] = num
                neg += 2

        return ans


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    ans = Solution().rearrangeArray(nums)
    print(ans)
