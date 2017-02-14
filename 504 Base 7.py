class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        num_less_than_0 = num<0
        num = abs(num)
        result = ''
        while True:
            if num == 0:
                break
            else:
                result = str(num % 7) + result
                num = int(num / 7)
        if num_less_than_0:
            return '-'+ result
        else:
            return result