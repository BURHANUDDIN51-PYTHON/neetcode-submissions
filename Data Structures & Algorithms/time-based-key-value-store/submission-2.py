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

        for v, t in reversed(self.timemap[key]):
            if t <= timestamp:
                return v

        return ""