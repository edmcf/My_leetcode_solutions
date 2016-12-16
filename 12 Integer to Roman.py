class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        thousand = ['', 'M', 'MM', 'MMM']
        hundred = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        ten = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        no = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        table = [thousand, hundred, ten, no]
        roman = ''
        strnum = str(num)
        for i in range(len(strnum)):
            roman = table[-i - 1][int(strnum[-i - 1])] + roman

        return roman