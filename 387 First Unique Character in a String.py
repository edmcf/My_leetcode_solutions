class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        ls = list(s)
        for i in ls:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        for i in range(len(ls)):
            if (ls[i] in d) and d[ls[i]] == 1:
                return i

        return -1