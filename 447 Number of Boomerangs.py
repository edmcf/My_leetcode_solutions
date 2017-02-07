class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        counter = 0

        if len(points) < 3:
            return counter

        for i in points:
            dict = {}
            for j in points:
                dis = (i[0] - j[0]) * (i[0] - j[0]) + (i[1] - j[1]) * (i[1] - j[1])
                if dis in dict:
                    dict[dis] += 1
                else:
                    dict[dis] = 1

            for k in dict:
                counter += (dict[k] * (dict[k] - 1))
        return counter