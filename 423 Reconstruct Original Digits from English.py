#  unfinised

class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = { }
        # make the hash table
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        num_list = [0,0,0,0,0,0,0,0,0,0]

        #use chr 'z' to count 0
        if 'z' in dic and dic['z'] != 0:
            num_list[0] = dic['z']
            dic['z'] -= num_list[0]
            dic['e'] -= num_list[0]
            dic['r'] -= num_list[0]
            dic['o'] -= num_list[0]

        #     use w to count 2
        if 'w' in dic and dic['w'] != 0:
            num_list[2] = dic['w']
            dic['t'] -= num_list[2]
            dic['w'] -= num_list[2]
            dic['o'] -= num_list[2]

        # use chr u to count 4
        if 'u' in dic and dic['u'] != 0:
            num_list[4] = dic['u']
            dic['f'] -= num_list[4]
            dic['o'] -= num_list[4]
            dic['u'] -= num_list[4]
            dic['r'] -= num_list[4]

        # use chr x to count 6
        if 'x' in dic and dic['x'] != 0:
            num_list[6] = dic['x']
            dic['s'] -= num_list[6]
            dic['i'] -= num_list[6]
            dic['x'] -= num_list[6]

        # use chr g to count 8
        if 'g' in dic and dic['g'] != 0:
            num_list[8] = dic['g']
            dic['e'] -= num_list[8]
            dic['i'] -= num_list[8]
            dic['g'] -= num_list[8]
            dic['h'] -= num_list[8]
            dic['t'] -= num_list[8]

        #     use f to count 5
        if 'f' in dic and dic['f'] != 0:
            num_list[5] = dic['f']
            dic['f'] -= num_list[5]
            dic['i'] -= num_list[5]
            dic['v'] -= num_list[5]
            dic['e'] -= num_list[5]

        # count 3
        if 'h' in dic and dic['h'] != 0:
            num_list[3] = dic['h']
            dic['t'] -= num_list[3]
            dic['h'] -= num_list[3]
            dic['r'] -= num_list[3]
            dic['e'] -= 2*num_list[3]

        #     use v to count 7
        if 'v' in dic and dic['v'] != 0:
            num_list[7] = dic['v']
            dic['s'] -= num_list[7]
            dic['e'] -= 2*num_list[7]
            dic['v'] -= num_list[7]
            dic['n'] -= num_list[7]

        if 'o' in dic and dic['o'] != 0:
            num_list[1] = dic['o']
            dic['o'] -= num_list[1]
            dic['n'] -= num_list[1]
            dic['e'] -= num_list[1]

        if 'i' in dic and dic['i'] != 0:
            num_list[9] = dic['i']

        result = ''
        for i in range(10):
            for j in range(num_list[i]):
                result += str(i)
        return result