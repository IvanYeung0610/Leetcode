"""
Ivan Yeung

19. Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        front = dummy
        back = dummy

        # front needs to be ahead n nodes so once front reaches the end, back is at target
        for i in range(n):
            if front != None:
                front = front.next

        # iterate until front is on the last node
        while front != None and front.next != None:
            front = front.next

            # this check ensures that back is at the node before we want to remove
            if front != None:
                back = back.next

        # remove the nth node from the back
        node_to_remove = back.next
        if node_to_remove == None:
            return None
        back.next = node_to_remove.next
        node_to_remove.next = None

        return dummy.next




