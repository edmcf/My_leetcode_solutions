class Solution(object):
    def islandPerimeter(self, gride):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        lj = len(gride[0])
        li = len(gride)

        for i in range(li):
            for j in range(lj):
                if gride[i][j] == 1:
                    if i ==0 :
                        perimeter +=1
                    elif gride[i-1][j] == 0:
                        perimeter +=1

                    if i == li-1:
                        perimeter += 1
                    elif gride[i+1][j] == 0:
                        perimeter += 1

                    if j == 0:
                        perimeter += 1
                    elif gride[i][j-1] == 0:
                        perimeter += 1

                    if j == lj -1:
                        perimeter += 1
                    elif gride[i][j+1] == 0:
                        perimeter += 1
        return perimeter