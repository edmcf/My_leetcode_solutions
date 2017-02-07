class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dicts = {}
        s = list(s)
        t = list(t)

        for i in s:
            if i in dicts:
                dicts[i] += 1
            else:
                dicts[i] = 1

        for i in t:
            if (i in dicts and dicts[i] != 0):
                dicts[i] -= 1
            else:
                return i