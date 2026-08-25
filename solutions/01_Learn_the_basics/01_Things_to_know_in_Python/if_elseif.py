"""
Title: If ElseIf
Topic: Basics
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/if-elseif?source=strivers-a2z-dsa-track
Date: 2026-08-26
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def studentGrade(self, marks):
        if marks >= 90:
            print("Grade A")
        elif marks >= 70:
            print("Grade B")
        elif marks >= 50:
            print("Grade C")
        elif marks >= 35:
            print("Grade D")
        else:
            print("Fail")


if __name__ == "__main__":
    marks = int(input())
    Solution().studentGrade(marks)
