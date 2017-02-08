class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = 0
        count = 0
        while True:
            if num == 0:
                break
            if (num >> 1) << 1 != num:
                pass
            else:
                result = result +(1 << count)
            num = num >> 1
            count += 1
        return result