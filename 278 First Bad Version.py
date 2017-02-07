# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
def inTheRange(start, end):
    if not isBadVersion(start - 1) == True and not isBadVersion(end) == False:
        return True
    else:
        return False


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while True:
            if end == start:
                return start
            elif end - start == 1:
                if not isBadVersion(start):
                    return end
                else:
                    return start

            if inTheRange(start, int(start + (end - start) / 2)):
                end = int(start + (end - start) / 2)
            elif inTheRange(int(start + (end - start) / 2), end):
                start = int(start + (end - start) / 2)
