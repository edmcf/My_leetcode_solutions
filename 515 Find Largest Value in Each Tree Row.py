# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # no root is given
        if not root:
            return []

        def has_no_son(node_list):
            for i in node_list:
                if i.left or i.right:
                    return False
            return True

        def get_largest_val(node_list):
            largest = node_list[0].val
            for i in node_list:
                if i.val > largest:
                    largest = i.val
            return largest

        traversal = [[root]]
        while True:
            if has_no_son(traversal[-1]):
                break
            else:
                temp = []
                for i in traversal[-1]:
                    if i.left:
                        temp.append(i.left)
                    if i.right:
                        temp.append(i.right)
                traversal.append(temp)

        result = []
        for i in traversal:
            result.append(get_largest_val(i))
        return result