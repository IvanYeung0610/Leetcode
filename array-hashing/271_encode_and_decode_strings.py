"""
Ivan Yeung

271. Encode and Decode Strings
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
"""
class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded_str = ""
        for string in strs:
            encoded_str += str(len(string))
            encoded_str += '|' # seperator
            encoded_str += string
        return encoded_str

    def decode(self, s: str) -> list[str]:
        res: list[str] = []
        index = 0

        while index < len(s):
            # get the length of the string
            string_len = ""
            while s[index] != '|':
                string_len += s[index]
                index += 1

            index += 1 # move to first char of actual string

            length = int(string_len)
            string = ""
            # add string to return list
            for i in range(length):
                string += s[index]
                index += 1
            res.append(string)

        return res
