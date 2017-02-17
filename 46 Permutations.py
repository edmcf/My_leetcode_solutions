class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        elif len(nums) == 2:
            return [nums,[nums[1],nums[0]]]

        else:
            result = []
            pre_permute = self.permute(nums[:-1])
            for i in pre_permute:
                # temp = i
                for j in range(len(pre_permute[0]) + 1):
                    temp = i[:]
                    temp.insert(j,nums[-1])
                    result.append(temp)
            return result