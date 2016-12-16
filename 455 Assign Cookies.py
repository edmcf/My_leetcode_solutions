class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        result = 0
        g.sort()
        s.sort()
        while True:
            if len(s) == 0 or len(g) == 0:
                break
            elif s[0] >= g[0]:
                s.pop(0)
                g.pop(0)
                result +=1
            elif s[0] < g[0]:
                s.pop(0)
        return result