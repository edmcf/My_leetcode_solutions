class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cons_set = set([])
        temp = 0
        for i in nums:
            if i == 0:
                cons_set.add(temp)
                temp = 0
            else:
                temp += 1
            cons_set.add(temp)
        return max(cons_set)