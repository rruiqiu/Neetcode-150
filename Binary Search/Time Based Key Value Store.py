class TimeMap:
    def __init__(self):
        # key: alice, [(1:happy), (3:sad)]
        self.data = {}
        # when we get, get the latest, largest that is less than

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append((timestamp, value))
        else:
            self.data[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.data:
            # perform binary search
            arr = self.data[key]
            l, r = 0, len(arr) - 1
            res = ""
            while l <= r:
                mid = (l + r) // 2
                if arr[mid][0] <= timestamp:
                    res = arr[mid][1]
                    l = mid + 1
                else:
                    r = mid - 1
            return res
        else:
            return ""
