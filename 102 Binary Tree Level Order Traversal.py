# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        def has_no_son(node_list):
            for i in node_list:
                if i.left or i.right:
                    return False
            return True

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

        for i in range(len(traversal)):
            for j in range(len(traversal[i])):
                traversal[i][j] = traversal[i][j].val
        return traversal