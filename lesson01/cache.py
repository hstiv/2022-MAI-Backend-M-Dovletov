class LRUCache:

    def __init__(self, capacity: int=10) -> None:
        self.cache = dict()
        self.capacity = capacity
        self.count = 0

    def get(self, key: str) -> str:
        return(self.cache[key] if key in self.cache else "")

    def set(self, key: str, value: str) -> None:
        if (self.count < self.capacity):
            self.cache[key] = value
            self.count += 1
        else:
            print('ERROR: Cache is full.')

    def rem(self, key: str) -> None:
        self.cache = self.cache.pop(key)
        self.capacity -= 1
