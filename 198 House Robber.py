class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        if len(nums) <= 2:
            return max(nums)

        rob = [nums[0], max(nums[:2])]
        i = 2
        while True:
            rob.append(max(rob[i - 1], rob[i - 2] + nums[i]))
            if len(nums) == len(rob):
                return rob[-1]
            i += 1