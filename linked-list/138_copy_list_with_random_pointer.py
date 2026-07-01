"""
Ivan Yeung

138. Copy List with Random Pointer
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

    val: an integer representing Node.val
    random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.
"""
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # iterate through the orignal list a build a hash map with Node keys and index values
        original_nodes: dict[Node, int] = {}
        cursor = head
        index = 0
        while cursor != None:
            original_nodes[cursor] = index
            index += 1
            cursor = cursor.next

        # iterate through the orignal list again to build the new list while tracking Nodes
        # that have already been created with another hashmap
        cursor = head
        index = 0
        dummy = Node(0) # dummy node that points to head of copied list
        new_cursor = dummy
        # hash mpa with index as the key and the copied Nodes as the value
        new_nodes: dict[int, Node] = {}
        while cursor != None:
            # Create the new node of assign it from the hashmap if already created
            if index in new_nodes:
                new_cursor.next = new_nodes[index]
            else:
                # create the node and add it to the dictionary
                new_cursor.next = Node(cursor.val)
                new_nodes[index] = new_cursor.next

            # get the index of the random node if it exists and set the new nodes random to
            # the random node if already created or make a new one
            if cursor.random != None:
                rand_index = original_nodes[cursor.random]
                # use the node in the dictionary if that index has already been created
                if rand_index in new_nodes:
                    new_cursor.next.random = new_nodes[rand_index]
                else:
                    new_rand_node = Node(cursor.random.val)
                    # add new node to dictionary with respective index as key
                    new_nodes[rand_index] = new_rand_node
                    # set the new nodes random to the copy of random
                    new_cursor.next.random = new_rand_node

            # increment the index and move cursor and new_cursor
            index += 1
            cursor = cursor.next
            new_cursor = new_cursor.next

        return dummy.next

