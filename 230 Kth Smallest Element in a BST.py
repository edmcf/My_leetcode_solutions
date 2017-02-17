# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        sorted_list = []
        stack = []
        # generate the stack
        while True:
            if not root:
                break
            else:
                stack.append(root)
                root = root.left

        while True:
            if len(sorted_list) == k:
                return sorted_list[-1]
            sorted_list.append(stack[-1])
            right = stack[-1].right
            stack.pop(-1)
            while right != None:
                stack.append(right)
                right = right.left

