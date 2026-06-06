"""
Ivan Yeung

20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []

        for char in s:
            if char == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False
            elif char == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False
            elif char == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    return False
            else:
                stack.append(char)

        if len(stack) == 0:
            return True

        return False

