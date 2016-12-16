class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

        ls = []
        for i in dict:
            ls.append([i, dict[i]])
        ls = sorted(ls, key=lambda x: x[1], reverse=True)

        topf = []
        for i in range(0, k):
            topf.append(ls[i][0])
        return topf