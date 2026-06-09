"""
Ivan Yeung

739. Daily Temperatures
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # monotonic stack storing tuple of (temp, index)
        stack: list[tuple[int, int]] = []
        answer: list[int] = []

        # iterating through the temperatures from the back to generate
        # the reverse of the output list
        for i in range(len(temperatures), 0, -1):
            curr_temp = (temperatures[i-1], i-1)
            # pop from stack until it is empty or the top is a higher temp
            while len(stack) != 0 and stack[-1][0] <=  curr_temp[0]:
                stack.pop()
            if len(stack) == 0: # there is no future day for higher temp
                answer.append(0)
            else:
                answer.append(stack[-1][1] - curr_temp[1])

            stack.append(curr_temp)

        answer.reverse() # reverse the list to get the right ordering

        return answer 

