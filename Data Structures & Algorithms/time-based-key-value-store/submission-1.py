class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.store[key] or timestamp < self.store[key][0][0]:
            return ""
        
        l, r = 0, len(self.store[key]) - 1
        while l <= r:
            m = (r + l) // 2
            if self.store[key][m][0] == timestamp:
                return self.store[key][m][1]
            elif self.store[key][m][0] > timestamp:
                r = m - 1
            else:
                l = m + 1
        
        return self.store[key][r][1]