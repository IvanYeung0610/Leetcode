"""
Ivan Yeung

49. Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""
class Solution:
    """
    # O(m * nlogn) solution
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_lists: dict[str, list[str]] = {} # dict to store grouped anagrams

        # for each word, sort alphabetically to get unique key to see if anagram
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_lists:
                anagram_lists[sorted_word].append(word)
            else:
                anagram_lists[sorted_word] = [word]

        # collect all lists into a list to return
        res: list[list[str]] = []
        for key in anagram_lists:
            res.append(anagram_lists[key])

        return res
    """
    # O(m * n) solution
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_lists: dict[frozenset, list[str]] = {} # dict to store grouped anagrams

        # for each word, create a frequency map with a dict to get unique key 
        # for unique anagram  NOTE: creating fixed 26 len array is more optimized
        for word in strs:
            letter_freq: dict[str, int] = {}
            # create frequency map
            for letter in word:
                if letter in letter_freq:
                    letter_freq[letter] += 1
                else:
                    letter_freq[letter] = 1
            # turn frequency map to a key
            key = frozenset(letter_freq.items())

            # add word to list based on created key
            if key in anagram_lists:
                anagram_lists[key].append(word)
            else:
                anagram_lists[key] = [word]

        # collect all lists into a list to return
        res: list[list[str]] = []
        for key in anagram_lists:
            res.append(anagram_lists[key])

        return res

