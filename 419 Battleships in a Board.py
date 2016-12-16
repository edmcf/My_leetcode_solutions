class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        w = len(board[0])
        h = len(board)
        counter = 0
        for i in range(h):
            for j in range(w):
                if board[i][j] == "X":
                    if i == 0 and j == 0:
                        counter += 1
                    if i == 0 and j != 0:
                        if board[i][j - 1] == ".":
                            counter += 1
                    if i != 0 and j == 0:
                        if board[i - 1][j] == ".":
                            counter += 1
                    if i != 0 and j != 0:
                        if board[i - 1][j] == "." and board[i][j - 1] == ".":
                            counter += 1

        return counter