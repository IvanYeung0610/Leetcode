"""
Ivan Yeung

424. Longest Repeating Character Replacement
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations
"""
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # We will be keeping track of the frequency of each
        # character while expanding the window
        char_freq: dict[str, int] = defaultdict(int)
        # We will be store the frequency of the most common character
        # in the window to determine if the window is valid
        max_freq = 0

        max_len = 0
        left = 0
        right = 0
        while right < len(s):
            # Add to frequency map
            char_freq[s[right]] += 1
            # Check if there is a new max
            max_freq = max(max_freq, char_freq[s[right]])
            # check if valid
            # check if (right - left) - max_freq <= k
            while (((right-left+1) - max_freq)  > k):
                # decrement from freq map
                char_freq[s[left]] -= 1
                # move window left boundary
                left += 1
            max_len = max(max_len, right - left + 1)
            # move right pointer
            right += 1

        return max_len
"""
NOTE: There isn't a need to update max_freq when shrinking the window because
the only time our max_len (the answer) will update is when we get a bigger
max_freq so it doesn't matter if it is wrong since it will update when
we actually need it for the new max_len.
"""
