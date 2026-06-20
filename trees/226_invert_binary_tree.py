"""
Ivan Yeung

226. Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left, root.right = right, left

        return root
