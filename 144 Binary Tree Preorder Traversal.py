# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasNoSon(self, root):
        if root.left == None and root.right == None:
            return True
        return False

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        tra = []
        result = []
        queue = [root]
        while True:
            # 如果queue[0]没有子节点，添加到tra中并从queue中删去
            if self.hasNoSon(queue[0]):
                tra.append(queue[0])
                queue.pop(0)
            else:
                # 如果queue[0]有右子节点
                if not queue[0].right == None:
                    queue.insert(1, queue[0].right)
                # 如果queue[0]有左子节点
                if not queue[0].left == None:
                    queue.insert(1, queue[0].left)
                # 添加到tra中并从queue中删去
                tra.append(queue[0])
                queue.pop(0)
            if queue == []:
                for i in tra:
                    result.append(i.val)
                return result