# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == []:
            return None
        elif len(nums) == 1:
            tree_node = TreeNode(nums[0])
            return tree_node
        else:
            root_index = (len(nums) - 1) >> 1
            left_tree = nums[:root_index]
            right_tree = nums[root_index + 1:]
            root = TreeNode(nums[root_index])
            root.left = self.sortedArrayToBST(left_tree)
            root.right = self.sortedArrayToBST(right_tree)
            return root