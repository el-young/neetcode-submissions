class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store.setdefault(key, []).append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store.get(key, [])
        l, r = 0, len(arr)
        while l < r:
            mid = l + (r - l) // 2
            if arr[mid][1] <= timestamp:
                l = mid + 1
            else:
                r = mid
        return arr[l - 1][0] if l > 0 else ""