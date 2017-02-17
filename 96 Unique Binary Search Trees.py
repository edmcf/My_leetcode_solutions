class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_of_solution = [1,1,2]
        if n <= 2:
            return num_of_solution[n]
        else:
            while True:
                if len(num_of_solution) == n + 1:
                    break
                solutions = 0
                for i in range(len(num_of_solution)):
                    solutions += num_of_solution[i] * num_of_solution[len(num_of_solution) - i - 1]
                num_of_solution.append(solutions)
        return num_of_solution[-1]