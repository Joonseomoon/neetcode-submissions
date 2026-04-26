class TimeMap:

    def __init__(self):
        self.hashmap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""

        l, r = 0, len(self.hashmap[key]) - 1 # binary search since we know timestamps are in increasing order
        recTimestampIndex = -1 # index of most recent value timestamp pair list
        while l <= r:
            m = l + ((r - l) // 2) # middle of remaining key list
            currTimestamp = self.hashmap[key][m][1] # current timestamp of middle
            if currTimestamp > timestamp:
                r = m - 1
            else:
                l = m + 1
                recTimestampIndex = m
        if recTimestampIndex == -1:
            return ""
        else:
            return self.hashmap[key][recTimestampIndex][0]
