import unittest
class BTNode:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

def get_bst_height(root:BTNode)->int:
    if root is None:
        return 0
    return 1 + max(get_bst_height(root.left), get_bst_height(root.right))

class TestBSTHeight(unittest.TestCase):
    def test_tree_with_5_nodes(self):
        root = BTNode(10,BTNode(7,BTNode(6),BTNode(8)),BTNode(11))
        assert get_bst_height(root) == 3
    def test_tree_with_10_nodes(self):
        root = BTNode(10,BTNode(9,BTNode(8),None),BTNode(11,BTNode(7,BTNode(6,BTNode(5,None),None),None),BTNode(12,None,BTNode(13,None,BTNode(14)))))
        assert get_bst_height(root) == 5
