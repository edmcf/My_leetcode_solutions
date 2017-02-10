class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []:
            return []
        elif len(nums) == 1:
            return [[],nums]
        else:
            temp = self.subsets(nums[0:-1])
            # temps = self.subsets(nums[0:-1])
            temps = temp
            for i in temps:
                i.append(nums[-1])
            temp.extend(temps)
            return temp