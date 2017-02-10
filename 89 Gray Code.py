class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        elif n == 1:
            return [0,1]
        else:
            temp = self.grayCode(n - 1)
            temps = list(reversed(temp))
            # you should add bit to the left of the number,if not, the leetcode will judge your solution wrong
            for i in range(len(temps)):
                temps[i] = temps[i] + len(temps)
            temp.extend(temps)
            return temp