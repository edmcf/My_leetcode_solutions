class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        hamming_distance = 0
        while True:
            if x == 0 and y == 0:
                break
            if ((x >> 1) << 1 != x and (y >> 1) << 1 == y) or ((x >> 1) << 1 == x and (y >> 1) << 1 != y):
                hamming_distance += 1
            x = x >> 1
            y = y >> 1
        return hamming_distance