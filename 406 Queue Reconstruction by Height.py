class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        harray = []
        sortedpeople = []
        people.sort(key=lambda x: x[1])
        for i in people:
            if i[0] not in harray:
                harray.append(i[0])
        harray.sort()
        harray.reverse()

        for i in harray:
            for j in people:
                if j[0] == i:
                    sortedpeople.insert(j[1], j)

        return sortedpeople