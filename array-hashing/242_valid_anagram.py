"""
Ivan Yeung

242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check that both are same size
        if (len(s) != len(t)):
            return False

        letter_count: dict[str, int] = {}
        # count each letter in s
        for letter in s:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1


        # Check that each letter exists in t
        for letter in t:
            if (letter in letter_count) and (letter_count[letter] > 0):
                letter_count[letter] -= 1
            else:
                return False

        return True

if __name__ == "__main__":
    test = Solution()
    print(test.isAnagram("anagram", "nagaram"))
