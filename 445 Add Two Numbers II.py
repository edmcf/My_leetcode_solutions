# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#List is acceptable
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 1 of them is empty
        if not l1:
            return l2
        if not l2:
            return l1

        def link_to_list(l):
            index = l
            listl = []
            while True:
                listl.append(index.val)
                if not index.next:
                    break
                else:
                    index = index.next
            return listl

        listl1 = link_to_list(l1)
        listl2 = link_to_list(l2)
        longer,shorter =None,None
        if len(listl1) >= len(listl2):
            longer = listl1
            shorter = listl2
        else:
            longer = listl2
            shorter = listl1
        minlen = min(len(listl1),len(listl2))
        for i in range(minlen):
            longer[-1 - i] += shorter[-1 - i]

        result = []
        for i in range(len(longer) - 1):
            if longer[-1 - i] >= 10:
                longer[-1 - i] -=10
                longer[-1 -i -1] += 1
        if longer[0] >= 10:
            longer[0] -= 10
            longer.insert(0,1)

        return longer
