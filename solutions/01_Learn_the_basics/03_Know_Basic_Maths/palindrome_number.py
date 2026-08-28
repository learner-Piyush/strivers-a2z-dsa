"""
Title: Palindrome Number
Topic: Basic Maths
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/palindrome-number?source=strivers-a2z-dsa-track
Date: 2026-08-28
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def isPalindrome(self, n):
        orignal = n
        reverse = 0

        while n > 0:
            digit = n % 10
            reverse = reverse * 10 + digit
            n //= 10
        
        return orignal == reverse


if __name__ == "__main__":
    n = int(input())
    print(Solution().isPalindrome(n))
