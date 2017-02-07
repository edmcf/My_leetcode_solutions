class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True

        ps = pt = 0

        while ps <= len(s) - 1 and pt <= len(t) - 1:
            if s[ps] == t[pt] and ps == len(s) - 1:
                return True
            elif s[ps] == t[pt]:
                pt += 1
                ps += 1
            elif s[ps] != t[pt]:
                pt += 1

        return False