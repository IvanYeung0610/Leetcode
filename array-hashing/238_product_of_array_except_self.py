"""
Ivan Yeung

238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        prefix: list of the product of all nums up to the index starting
        from index 0 of nums list. Padded with 1 at the front.
        Ex:
            nums: [1, 2, 3, 4]
            prefix: [1, 1, 2, 6, 24]

        postfix: list of the product of all nums down to the index starting
        from the last index of nums list. Padded with 1 at the back.
        Ex:
            nums: [1, 2, 3, 4]
            postfix: [24, 24, 12, 4, 1]

        """
        prefix: list[int] = [1]
        postfix: list[int] = [1]

        # generate the prefix and postfix products of the nums list
        reversed_nums = nums[::-1]
        for i in range(len(nums)):
            prefix.append(nums[i] * prefix[-1])
            postfix.append(nums[(len(nums)-1)-i] * postfix[-1])
        postfix.reverse()

        print(prefix)
        print(postfix)

        # generate the output list by multiplying the index before in the prefix and the
        # index after in the postfix
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * postfix[i+1])

        return res

if __name__ == "__main__":
    soln = Solution()
    soln.productExceptSelf([1, 2, 3, 4])
