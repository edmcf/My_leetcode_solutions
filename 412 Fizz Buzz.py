class Solution(object):
    def fizzBuzz(self, n):
        fB = []
        for i in range(1,n+1):
            if (i%3 == 0 | i%5 == 0):
                fB.append("FizzBuzz")
            elif (i%3 == 0):
                fB.append("Fizz")
            elif (i%5 == 0):
                fB.append("Buzz")
            else:
                fB.append(str(i))
        return fB