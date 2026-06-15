"""
Ivan Yeung

21. Merge Two Sorted Linked Lists
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None

        # create a variable to store the head to return as the answer
        head = list1
        if list1 == None:
            head = list2

        cursor1 = list1
        cursor2 = list2
        while cursor1 != None and cursor2 != None:
            if cursor1.val < cursor2.val:
                if prev_node == None:
                    head = cursor1
                else:
                    prev_node.next = cursor1
                prev_node = cursor1
                cursor1 = cursor1.next
            else:
                if prev_node == None:
                    head = cursor2
                else:
                    prev_node.next = cursor2
                prev_node = cursor2
                cursor2 = cursor2.next

        # connect the list to the remaining end if one was larger
        if prev_node != None and cursor1 != None:
            prev_node.next = cursor1
        if prev_node != None and cursor2 != None:
            prev_node.next = cursor2

        return head

# NOTE: You can make a dummy node as a starting value for the prev_node to
# make the implementation cleaner in the code since we won't have to do
# as many checks since prev_node will then always be a valid value
