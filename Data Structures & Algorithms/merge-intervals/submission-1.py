class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        i = 0
        while i < len(intervals):
            newInterval = intervals[i]
            while i < len(intervals) - 1 and newInterval[1] >= intervals[i + 1][0]:
                newInterval = [
                    min(newInterval[0], intervals[i + 1][0]),
                    max(newInterval[1], intervals[i + 1][1])
                ]
                i += 1
            res.append(newInterval)
            i += 1
        return res