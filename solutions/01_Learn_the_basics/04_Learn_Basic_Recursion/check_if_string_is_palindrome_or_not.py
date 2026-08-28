"""
Title: Check if String is Palindrome or Not
Topic: Recursion
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/check-if-string-is-palindrome-or-not-?source=strivers-a2z-dsa-track
Date: 2026-08-28
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:    
    def palindromeCheck(self, s):
        #your code goes here
        def check(left, right):
            if left >= right:
                return True

            if s[left] != s[right]:
                return False

            return check(left + 1, right - 1)

        return check(0, len(s) - 1)


if __name__ == "__main__":
    s = input()
    print(Solution().palindromeCheck(s))
