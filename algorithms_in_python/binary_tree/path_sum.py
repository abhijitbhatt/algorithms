class BTNode:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right
# https://www.geeksforgeeks.org/find-all-root-to-leaf-path-sum-of-a-binary-tree/
def path_sum(root):
    results = []
    def _is_leaf(node):
        return (True if not node.left and not node.right else False)
    def path_sum_recursive(root,running_sum=0):
        if not root:
            return
        if root.left:
            path_sum_recursive(root.left,running_sum + root.value)
        if root.right:
            path_sum_recursive(root.right,running_sum + root.value)
        #if _is_leaf(root):
        results.append(running_sum + root.value)
    path_sum_recursive(root)
    return results

root = BTNode(30,BTNode(10,BTNode(3),BTNode(16)),BTNode(50,BTNode(40),BTNode(60)))
print(path_sum(root))