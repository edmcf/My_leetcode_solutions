class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 0
        if num < 0:
            return False
        return pow(num,0.5) % 1 == 0