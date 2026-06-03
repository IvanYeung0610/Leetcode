"""
Ivan Yeung

347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""
class Solution:
    """
    # O(nlogn) solution
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq: dict[int, int] = {} # [number, frequency]
        # Create a frequency map
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        sorted_keys = sorted(freq, key=lambda x: freq[x], reverse=True)
        # Alternative: sorted(freq, key=freq.__getitem__, reverse=True)

        # Return the k most frequent elements
        return sorted_keys[:k]
    """
    # O(n) solution
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # create a bucket system to put nums based on frequency
        bucket: list[list[int]] = [[] for _ in range(len(nums))]

        freq: dict[int, int] = {} # [number, frequency]
        # Create a frequency map
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # place each num in bucket corresponding to frequency
        for key in freq:
            bucket[freq[key] - 1].append(key)

        # get the k top frequent nums and return
        res: list[int] = []
        index = len(nums) - 1
        nums_needed = k
        while nums_needed > 0 and index >= 0:
            inner_index = 0
            while nums_needed > 0 and inner_index < len(bucket[index]):
                res.append(bucket[index][inner_index])
                nums_needed -= 1
                inner_index += 1
            index -= 1

        return res



