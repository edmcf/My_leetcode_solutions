class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            result = [[1], [1, 1]]
            ls = [1, 1]
            while True:
                ls = generateE(ls)
                result.append(ls)
                if len(result) == numRows:
                    return result


def generateE(e):
    ls = []
    l = len(e)
    for i in range(l):
        if (i == 0):
            ls.append(1)
        else:
            ls.append(e[i - 1] + e[i])
    ls.append(1)
    return ls
