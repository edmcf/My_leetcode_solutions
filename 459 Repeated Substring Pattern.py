class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        l = len(str)
        ls = []  # l 的所有因数
        for i in range(1, l):
            if l % i == 0:
                ls.append(i)

        ls.reverse()

        for i in ls:
            sub = str[:i]
            cons = ''
            for j in range(int(l / i)):
                cons += sub
            if cons == str:
                return True
        return False