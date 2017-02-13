class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [-1] * len(nums)
        stack = nums[:]
        for i in range(len(nums)):
            while stack != [] and stack[0] <= nums[-1 - i]:
                stack.pop(0)
            if stack != []:
                result[-1 - i] = stack[0]
            stack.insert(0,nums[-1 - i])
        return result
