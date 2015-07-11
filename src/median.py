__author__ = 'kafka'
import heapq as hq

class Median:
    """Adds occurrences to the upper or lower heaps."""

    def __init__(self):
        """Initialize upper and lower heaps and
        set switch that is 'True' if both heaps are the same size."""

        self.lower = []
        self.upper = []
        self.even = True

    def add(self, num):
        """Use negative numbers for self.lower.
        The median will be either at the bottom of a heap,
        or the average of both bottom entries.
        heappushpop will pop the median from the bottom"""

        if self.even:
            if not self.lower:
                hq.heappush(self.lower, -1*num)
            elif num > -1*self.lower[0]:
                x = hq.heappushpop(self.upper, num)
                hq.heappush(self.lower, -1*x)
            else:
                hq.heappush(self.lower, -1*num)
            self.even = False
        else:
            if num > -1*self.lower[0]:
                hq.heappush(self.upper, num)
            else:
                x = hq.heappushpop(self.lower, -1*num)
                hq.heappush(self.upper, -1*x)
            self.even = True

    def get(self):
        """return the median"""

        if self.even:
            return (self.upper[0]-self.lower[0])/2.0
        else:
            return -1*self.lower[0]
