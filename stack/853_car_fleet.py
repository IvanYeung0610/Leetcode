"""
Ivan Yeung

853. Car Fleet
There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.

You are given two integer arrays position and speed, both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.

A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.

A car fleet is a single car or a group of cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.

If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.

Return the number of car fleets that will arrive at the destination.
"""
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        combined_list: list[tuple[int, int]] = []
        for i in range(len(position)):
            combined_list.append((position[i], speed[i]))

        combined_list.sort(reverse=True) # sort w/ biggest pos first

        # Iterate through list and add to monotonically decreasing stack
        # Monotonically decreasing based on fleet
        stack: list[tuple[int, int]] = []
        for car in combined_list:
            if len(stack) == 0:
                stack.append(car)
            else:
                if car[0] == stack[-1][0]:
                    # edge case of two cars starting at the same position
                    if car[1] < stack[-1][0]:
                        stack.pop()
                        stack.append(car)
                elif car[1] <= stack[-1][1]:
                    # car ahead is faster or same speed
                    # so the current car can't catch up and form its own fleet
                    stack.append(car)
                else:
                    # check if car can catch up the car ahead
                    # otherwise it forms its own fleet

                    # we are checking time it takes for both cars
                    # to reach the target. If the time for the current car
                    # is less, then we know it will catch up
                    time_to_target_ahead = (target - stack[-1][0]) / stack[-1][1]
                    time_to_target_behind = (target - car[0]) / car[1]
                    if (time_to_target_ahead < time_to_target_behind):
                        # the current car won't catch the fleet in front
                        # and thus forms its own fleet
                        stack.append(car)

        return len(stack)

