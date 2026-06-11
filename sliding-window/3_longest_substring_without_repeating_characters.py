"""
Ivan Yeung

3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest without duplicate characters.
substring: A substring is a contiguous non-empty sequence of characters within a string.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index: dict[str, int] = {} # dictionary keeping track of characters
        left = 0
        right = 0
        longest_len = 0

        while right < len(s):
            if s[right] in char_index:
                # check if the recorded index has already been passed
                if char_index[s[right]] >= left:
                    # move left to index after repeating character if it hasn't already been passed
                    left = char_index[s[right]] + 1
                # set the new index for the character
                char_index[s[right]] = right
            else:
                # set the index for the first occurence of the character
                char_index[s[right]] = right
            longest_len = max(longest_len, (right - left) + 1)
            right += 1

        return longest_len
