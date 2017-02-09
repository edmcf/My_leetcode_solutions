# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root == None:
            return []
        elif root.left == None and root.right == None:
            return [root.val]
        else:
            result = self.inorderTraversal(root.left)
            result.extend([root.val])
            result.extend(self.inorderTraversal(root.right))
            return result