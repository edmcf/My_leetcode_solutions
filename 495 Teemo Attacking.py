class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        result = duration
        if timeSeries == []:
            return 0
        if len(timeSeries) == 1:
            return duration
        for i in range(len(timeSeries) - 1):
            if timeSeries[i + 1] - timeSeries[i] >= duration:
                result += duration
            else:
                result += (timeSeries[i + 1] - timeSeries[i])
        return result