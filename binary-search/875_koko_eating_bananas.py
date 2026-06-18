"""
Ivan Yeung

875. Koko Eating Bananas
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
"""
import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # searching for the slowest speed between 1 and the largest pile size
        max_speed = max(piles)

        # Optimization: if list size is the number of hours, eating speed has to be the largest pile
        if len(piles) == h:
            return max_speed

        left = 1
        right = max_speed

        while left <= right:
            pivot = left + ((right - left) // 2)
            eating_time = self.eatingTime(piles, pivot)

            if eating_time > h:
                left = pivot + 1
            else: # valid eating speed with pivot
                # check if speed before is also valid, if it isn't you found the slowest speed
                if pivot - 1 == 0 or self.eatingTime(piles, pivot - 1) > h:
                    return pivot

                right = pivot - 1

        return 0 # this line should never be reached

    # Given list of piles and eating speed, return the number of hours to eat all bananas
    def eatingTime(self, piles: list[int], eating_speed: int) -> int:
        total_time = 0

        for pile in piles:
            if pile < eating_speed:
                total_time += 1
            else:
                total_time += math.ceil(pile / eating_speed)

        return total_time

# NOTE: Instead of check if the previous eating speed is valid to determine we still need to search,
# we can just keep running through the binary search and returned a stored minimun after the loop
