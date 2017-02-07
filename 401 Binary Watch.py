class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ls = []
        for i in range(12):
            for j in range(60):
                if bin(i).count('1') + bin(j).count('1') == num:
                    if j < 10:
                        s = str(i) + ":0" + str(j)
                    else:
                        s = str(i) + ":" + str(j)
                    ls.append(s)

        return ls
