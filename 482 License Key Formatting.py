class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = S.upper()
        list_of_s = list(s)
        index = 0
        # clear all the breaks
        while True:
            if index >= len(list_of_s):
                break
            if list_of_s[index] == '-':
                list_of_s.pop(index)
            else:
                index += 1

        result = ''
        if list_of_s != []:
            lenght_of_first_group = len(list_of_s) % K
            for i in range(lenght_of_first_group):
                result += list_of_s[0]
                list_of_s.pop(0)
            if list_of_s == []:
                return result
            for i in range(int(len(list_of_s) / K)):
                temp = list_of_s[K * i:K * (i + 1)]
                result += '-'
                for i in temp:
                    result += i
            if result[0] == '-':
                return result[1:]
        return result