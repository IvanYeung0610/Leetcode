"""
Ivan Yeung

128. Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
"""
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Move all numbers into a set for O(1) search
        nums_set: set[int] = set(nums)

        # Look for potential starting nums (nums that don't have a num-1)
        potential_starts: list[int] = []
        for num in nums_set:
            if (num-1) not in nums_set:
                potential_starts.append(num)

        # find the max sequence among potential starting nums
        max_seq_len = 0
        for start in potential_starts:
            seq_len = 0
            while start in nums_set:
                start += 1
                seq_len += 1
                if seq_len > max_seq_len:
                    max_seq_len = seq_len

        return max_seq_len



