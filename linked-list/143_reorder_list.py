"""
Ivan Yeung

143. Reorder List
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Storing nodes to be referenced in a stack
        stack: list[ListNode] = []
        cursor = head
        while cursor != None:
            stack.append(cursor)
            cursor = cursor.next

        # Reorder the list
        cursor = head
        while cursor != None and cursor.next != None:
            reorderedNext = stack.pop()

            # if we reach the current cursor, then we are done
            if reorderedNext == cursor:
                return

            # unlink the reorderedNext from original previous
            reorderedNextPrev = stack.pop()
            reorderedNextPrev.next = None
            stack.append(reorderedNextPrev) # basically replicating a peek by re appending

            nextCursor = cursor.next # the next value that we go to to reorder

            # add the reorderedNext between the cursor and cursor.next
            reorderedNext.next = cursor.next
            cursor.next = reorderedNext

            cursor = nextCursor

        return

