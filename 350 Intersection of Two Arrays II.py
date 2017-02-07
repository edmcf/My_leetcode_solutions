class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        table1 = {}
        table2 = {}
        result = []
        for i in nums1:
            if i in table1:
                table1[i] += 1
            else:
                table1[i] = 1

        for i in nums2:
            if i in table2:
                table2[i] += 1
            else:
                table2[i] = 1

        for i in table1:
            if i in table2:
                for j in range(min(table1[i], table2[i])):
                    result.append(i)

        return result
