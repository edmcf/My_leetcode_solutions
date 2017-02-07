class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        pointer = 0
        counter = 0
        while True:
            if pointer == len(s):
                return counter
            if pointer == 0:
                if not s[pointer] == ' ':
                    counter += 1
            else:
                if (not s[pointer] == ' ') and s[pointer - 1] == ' ':
                    counter += 1
            pointer +=1