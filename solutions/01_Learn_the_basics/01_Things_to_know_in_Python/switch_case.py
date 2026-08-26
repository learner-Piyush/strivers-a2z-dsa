"""
Title: Switch Case
Topic: Basics
Difficulty: Easy
Source: https://takeuforward.org/plus/dsa/problems/switch-case?source=strivers-a2z-dsa-track
Date: 2026-08-26
"""

# TODO: solve here.
# (Metadata header gets added automatically when you `git commit` this file
# for the first time — the pre-commit hook will ask for it.)


class Solution:
    def whichWeekDay(self, day):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        if 1 <= day <= 7:
            print(days[day - 1])
        else:
            print("Invalid")


if __name__ == "__main__":
    day = int(input())
    Solution().whichWeekDay(day)
