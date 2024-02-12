# https://leetcode.com/problems/count-good-nodes-in-binary-tree/?envType=study-plan-v2&envId=leetcode-75

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_node_count = 0
        def goodNodesRecursive(root:TreeNode, max_value=float('-inf')):
            nonlocal good_node_count
            if not root:
                return
            if root.left:
                goodNodesRecursive(root.left,max(max_value,root.val))
            if root.right:
                goodNodesRecursive(root.right,max(max_value,root.val))
            if root.val >= max_value:
                good_node_count += 1
        goodNodesRecursive(root)
        return good_node_count


# root = TreeNode(3,TreeNode(1,TreeNode(3),None),TreeNode(4,TreeNode(1),TreeNode(5)))
# Solution().postorder(root)
#
# root = TreeNode(3,TreeNode(3,TreeNode(4),TreeNode(2)),None)
# Solution().postorder(root)

root = TreeNode(1,TreeNode(3,TreeNode(9),None),None)
Solution().postorder(root)