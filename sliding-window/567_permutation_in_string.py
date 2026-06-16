"""
Ivan Yeung

567. Permutation in String
Given two strings s1 and s2, return true if s2 contains a of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
"""
from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # permutation not possible if second string is smaller
        if len(s1) > len(s2):
            return False

        s1_freq: list[int] = [0] * 26
        s2_wind_freq: list[int] = [0] * 26

        # Get the letter frequency for s1
        for letter in s1:
            s1_freq[ord(letter)-ord('a')] += 1

        # Get the letter frequency for initial window in s2
        for i in range(len(s1)):
            s2_wind_freq[ord(s2[i])-ord('a')] += 1

        if s1_freq == s2_wind_freq:
            return True

        left = 1
        right = len(s1)
        # move window until matching frequency or the end has been reached
        while right < len(s2):
            # remove past letter and add new one
            s2_wind_freq[ord(s2[left-1])-ord('a')] -= 1
            s2_wind_freq[ord(s2[right])-ord('a')] += 1
            # check if a permutation
            if s1_freq == s2_wind_freq:
                return True
            # move the window
            right += 1
            left += 1

        return False

# NOTE: Technically comparing the two frequency lists is constant since it will always be a fixed
# size of 26 but it could be more efficient by keeping track of the number of matches and updating it
# as we shift the window. This would only require a single check rather than 26 every iteration.



