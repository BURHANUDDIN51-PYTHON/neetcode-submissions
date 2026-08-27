from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key: 
            self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # return the key -> value with the timestamp or the closest 
        if key not in self.timemap:
            return ""

        # Binary search to find the results 
        res = ""
        l, r = 0, len(self.timemap[key]) - 1
        while (l <= r):
            mid = l + (r - l) // 2
            if self.timemap[key][mid][1] <= timestamp:
                res = self.timemap[key][mid][0]
                l = mid + 1
            else: 
                r = mid - 1

        return res