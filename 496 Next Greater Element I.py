class Solution(object):
    def find_next_greater_element(self, num, nums):
        start = 0
        for i in range(len(nums)):
            if num == nums[i]:
                start = i
                break
        for i in range(start, len(nums)):
            if nums[i] > num:
                return nums[i]
        return -1

    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in findNums:
            result.append(self.find_next_greater_element(i, nums))
        return result