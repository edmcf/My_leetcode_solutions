class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = []

        if len(num1) >= len(num2):
            lls = list(num1)
            lls.insert(0,'0')
            sls = list(num2)
            sls.insert(0,'0')
        else:
            lls = list(num2)
            lls.insert(0, '0')
            sls = list(num1)
            sls.insert(0, '0')

        for i in range(len(lls) - len(sls)):
            sls.insert(0,'0')

        for i in range(len(lls)):
            result.append(int(lls[i]) + int(sls[i]))

        for i in range(len(lls)):
            if result[len(lls)- 1 - i] >= 10:
                result[len(lls) - 1 - i] -= 10
                result[len(lls) - 2 - i] += 1

        if result[0] == 0:
            result.pop(0)

        output = ''
        for i in result:
            output += str(i)
        return output