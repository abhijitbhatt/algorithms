# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional
# Definition for a binary tree node.
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self,root):
        sorted_array = []
        min_abs_val = float('inf')
        def traverse_recursive(root):
            nonlocal min_abs_val
            if root is None:
                return
            traverse_recursive(root.left)
            if len(sorted_array) > 0:
                min_abs_val = min(min_abs_val, abs(sorted_array[-1] - root.val))
            sorted_array.append(root.val)
            traverse_recursive(root.right)
        traverse_recursive(root)
        return min_abs_val

class TestMinAbsDiff(unittest.TestCase):
    def test_non_adjacent_nodes(self):
        tree = TreeNode(236,TreeNode(104,None,TreeNode(227)),TreeNode(701,None,TreeNode(911)))
        assert Solution().getMinimumDifference(tree) == 9
    def test_adjacent_nodes(self):
        tree = TreeNode(4,TreeNode(2,TreeNode(1),TreeNode(3)),TreeNode(6))
        assert Solution().getMinimumDifference(tree) == 1


