"""
Ivan Yeung

239. Sliding Window Maximum
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
"""
import heapq
from collections import deque

class Solution:
    """
    # O(nlogn) solution using heaps
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # solved using a max heap storing the tuple (value, index)
        max_heap = []
        res: list[int] = []

        # setup the sliding window to the size of k by adding initial window values to heap
        left = 1
        right = k
        for i in range(k):
            heapq.heappush_max(max_heap, (nums[i], i))

        # simulate polling by popping and adding back
        curr_max = heapq.heappop_max(max_heap)
        res.append(curr_max[0])
        heapq.heappush_max(max_heap, curr_max)

        # move the window until end of array
        while right < len(nums):
            # add new value from extending window right
            heapq.heappush_max(max_heap, (nums[right], right))

            # NOTE: We don't have worry about removing the value left behind since
            # we to the heap with the index so we can determine if a max is outside the
            # window when we are trying to find the current window's max

            # pop until we have a max that is within index and add it to res list
            curr_max = heapq.heappop_max(max_heap)
            while curr_max[1] < left:
                curr_max = heapq.heappop_max(max_heap)

            # add the value back after adding to res
            res.append(curr_max[0])
            heapq.heappush_max(max_heap, curr_max)

            left += 1
            right += 1

        return res
    """
    # O(n) solution using a deque
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # Using a deque to store index of the values that have been covered so far.
        # The deque will be strictly decreasing. If we find a larger values remove them
        # and add the value
        deq = deque()
        res = []

        left = 0
        right = 0
        while right < len(nums):
            # remove indexes from the deque outside of window
            while len(deq) != 0 and deq[0] < left:
                deq.popleft()

            # add new element at right after removing previous elements that are smaller
            while len(deq) != 0 and nums[deq[-1]] < nums[right]:
                deq.pop()
            deq.append(right)

            # window size is at k
            if (right - left + 1) == k:
                # the max is at the front of the deque
                res.append(nums[deq[0]])
                # move the left side right
                left += 1

            # move the window right
            right += 1

        return res

