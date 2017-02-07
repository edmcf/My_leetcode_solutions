class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        table = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ')
        ls = list(s)
        counter = 0
        for i in ls:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

        for i in dict:
            if i in dict and (dict[i] % 2 == 1):
                counter += 1

        if counter == 0:
            return len(ls)
        else:
            return len(ls) - counter + 1