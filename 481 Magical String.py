class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n <= 3:
            return 1

        #used to generate the magicalstrin
        def ge_magical_string(n):
            magic_s = [1,2,2]
            index = 2
            while True:
                if len(magic_s) >= n:
                    break
                if magic_s[index] == 2:
                    if magic_s[-1] == 1:
                        magic_s.extend([2,2])
                    else:
                        magic_s.extend([1,1])
                else:
                    if magic_s[-1] == 1:
                        magic_s.append(2)
                    else:
                        magic_s.append(1)
                index += 1
            return magic_s

        count = 0
        magic_string = ge_magical_string(n)
        if len(magic_string) > n:
            magic_string.pop(-1)
        for i in magic_string:
            if i == 1:
                count += 1
        return count