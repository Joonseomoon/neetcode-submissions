class TimeMap:

    def __init__(self):
        self.hashmap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        
        if self.hashmap[key][-1][1] <= timestamp:
            return self.hashmap[key][-1][0]
        else:
            return ""
