class Solution(object):
    def isslice(self, s):
        if len(s) < 3:
            return False
        dif = s[1] - s[0]
        for i in range(len(s) - 1):
            if s[i + 1] - s[i] != dif:
                return False
        return True

    def countslice(self, s):
        counter = 0
        for i in range(len(s) - 2):
            if self.isslice(s[-3 - i:]):
                counter += 1
            else:
                return counter
        return counter

    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0;
        table = [0, 0, 0]
        while len(table) <= len(A):
            table.append(table[-1] + self.countslice(A[:len(table)]))

        return table[-1]