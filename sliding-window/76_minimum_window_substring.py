"""
Ivan Yeung

76. Minimum Window Substring
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
"""
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if s is bigger than t then return empty string
        if len(t) > len(s):
            return ""


        # setup inital frequency maps for both strings and the variables (have and need)
        t_freq: dict[str, int] = defaultdict(int)
        window_freq: dict[str, int] = defaultdict(int)

        for letter in t:
            t_freq[letter] += 1

        """
        Have is the number of letters that match with the same amount and need is the number
        of distinct letters in s. Have is only incremented when the frequency for a character
        match exactly.
        """
        have = 0
        need = len(t_freq.keys())

        # sliding window to find the smallest substring that contains every character in s
        left = 0
        right = 0
        res: str = ""
        while right < len(s):
            if s[right] in t_freq: # only need to keep track of relevant characters
                # increment right until we have a valid substring
                window_freq[s[right]] += 1
                # update have variable if values match
                if window_freq[s[right]] == t_freq[s[right]]:
                    have += 1

            # start moving the left point until we have an invalid substring while updating res
            # if have == need
            while have == need:
                # update res if current window is smaller
                if res == "" or (len(res) > (right - left + 1)):
                    res = s[left:right+1]
                    # NOTE: you can store the indicies instead of string splicing ever time we
                    # find a better substring for a faster time

                # shrink the left edge and update the have variable if necessary
                if s[left] in t_freq: # only keeping track of characters found in t
                    if window_freq[s[left]] == t_freq[s[left]]:
                        have -= 1
                    window_freq[s[left]] -= 1

                left += 1

            right += 1

        return res
