class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        def order(matrix,D,W,flag):
            order_list = []
            # before the left-bottom corner
            #from the bottom to the top
            if flag < D:
                j = 0
                while True:
                    if flag - j < 0 or j >= W:
                        break
                    order_list.append(matrix[flag - j][j])
                    j += 1
            #after the left-bottom cornor
            #from the bottom to the top
            else:
                j = 0
                while True:
                    if (D - 1) - j < 0 or flag - (D - 1) + j >= W:
                        break
                    order_list.append(matrix[(D - 1) - j][flag - (D - 1) + j])
                    j += 1
            if flag % 2 == 1:
                order_list = reversed(order_list)
            return order_list

        temp =[]
        result = []
        if matrix == []:
            return []
        elif matrix[0] == []:
            return []
        D = len(matrix)
        W = len(matrix[0])
        count = D + W - 1
        for i in range(count):
            temp.append(order(matrix,D,W,i))
        for i in temp:
            for j in i:
                result.append(j)
        return result