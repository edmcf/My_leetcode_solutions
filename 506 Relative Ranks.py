class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        dic = {}
        result = []
        copy_nums = nums
        nums = sorted(nums,reverse = True)
        for i in range(len(nums)):
            dic[nums[i]] = i + 1
        for i in copy_nums:
            if dic[i] == 1:
                result.append("Gold Medal")
            elif dic[i] == 2:
                result.append("Silver Medal")
            elif dic[i] == 3:
                result.append("Bronze Medal")
            else:
                result.append(str(dic[i]))
        return result
