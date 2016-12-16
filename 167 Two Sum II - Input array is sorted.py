class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        result = [0, 0]
        for i in range(len(numbers)):
            dict[numbers[i]] = i

        for i in range(len(numbers)):
            if target - numbers[i] in dict:
                result[0] = i + 1
                result[1] = dict[target - numbers[i]] + 1
                break
        return result