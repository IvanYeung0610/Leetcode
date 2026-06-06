"""
Ivan Yeung

125. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        back = len(s) - 1

        while front < len(s) and not s[front].isalnum():
            front += 1
        while back > 0 and not s[back].isalnum():
            back -= 1

        while front < back:
            if s[front].lower() != s[back].lower():
                return False

            # move two pointers towards each other
            front += 1
            back -= 1
            while front < len(s) and not s[front].isalnum():
                front += 1
            while back > 0 and not s[back].isalnum():
                back -= 1


        return True
