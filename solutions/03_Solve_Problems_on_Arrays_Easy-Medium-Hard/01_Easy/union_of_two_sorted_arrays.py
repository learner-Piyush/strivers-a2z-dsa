"""
Title: Union of two sorted arrays
Topic: Arrays
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/union-of-two-sorted-arrays?source=strivers-a2z-dsa-track
Date: 2026-09-01
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def unionArray(self, nums1, nums2):
        i = j = 0
        result = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                value = nums1[i]
                i += 1
            elif nums2[j] < nums1[i]:
                value = nums2[j]
                j += 1
            else:
                value = nums1[i]
                i += 1
                j += 1

            if not result or result[-1] != value:
                result.append(value)

        while i < len(nums1):
            if not result or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1

        while j < len(nums2):
            if not result or result[-1] != nums2[j]:
                result.append(nums2[j])
            j += 1

        return result


if __name__ == "__main__":
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    print(Solution().unionArray(nums1, nums2))
