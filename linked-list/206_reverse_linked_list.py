"""
Ivan Yeung

206. Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # O(n) space solution
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     reverse = None
    #     prev_node = None
    #     while head != None:
    #         reverse = ListNode(head.val, prev_node)
    #         # Store the newly copied node before making a new node for the next value
    #         prev_node = reverse
    #         head = head.next
    #
    #     return reverse

    # O(1) space solution
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        # switch the pointing as we iterate through each Node
        # not making an entirely new list
        while curr != None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev
