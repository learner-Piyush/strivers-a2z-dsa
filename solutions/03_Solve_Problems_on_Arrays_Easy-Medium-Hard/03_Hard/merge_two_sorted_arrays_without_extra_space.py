"""
Title: Merge two sorted arrays without extra space
Topic: Arrays
Difficulty: Medium
Source: https://takeuforward.org/plus/dsa/problems/merge-two-sorted-arrays-without-extra-space?source=strivers-a2z-dsa-track
Date: 2026-09-15
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


if __name__ == "__main__":
    # Input: m and n
    m, n = map(int, input().split())

    # Input nums1 (size m + n)
    nums1 = list(map(int, input().split()))

    # Input nums2 (size n)
    nums2 = list(map(int, input().split()))

    Solution().merge(nums1, m, nums2, n)

    print(nums1)
