class Solution(object):
    def isHappy(self, n):
        s = set([])
        while True:
            if get_Bitsum(n) in s:
                return False
            elif get_Bitsum(n) == 1:
                return True
            else:
                s.add(get_Bitsum(n))
                n = get_Bitsum(n)


def get_Bitsum(a):
    Bitsum = 0
    while True:
        Bitsum += (a % 10) * (a % 10)
        a = (a - a % 10) / 10
        if a == 0:
            break
    return int(Bitsum)
