class TimeMap:

    def __init__(self):
        self.hashmap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.hashmap[key]) - 1 # binary search since we know timestamps are in increasing order
        res = ""

        while l <= r:
            m = l + ((r - l) // 2) # middle of remaining key list
            currTimestamp = self.hashmap[key][m][1] # current timestamp of middle
            if currTimestamp > timestamp:
                r = m - 1
            elif currTimestamp == timestamp:
                res = self.hashmap[key][m][0]
                break
            else:
                l = m + 1
                res = self.hashmap[key][m][0]
        return res
