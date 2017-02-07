class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = [1]
        p2, p3, p5 = 0, 0, 0
        while len(table) < n:
            m = min(table[p2] * 2, table[p3] * 3, table[p5] * 5)
            table.append(m)
            if m == table[p2] * 2:
                p2 += 1
            if m == table[p3] * 3:
                p3 += 1
            if m == table[p5] * 5:
                p5 += 1

        return table[-1]