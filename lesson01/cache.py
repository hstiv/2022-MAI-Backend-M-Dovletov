from tokenize import String


class LRUCache:

    def __init__(self, capacity: int=10) -> None:
        self.cache = {}
        self.capacity = capacity

    def get(self, key: str) -> str:
        return self.cache.get(key) if key in self.cache else "" #Bug

    def set(self, key: str, value: str) -> None:
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) + 1 > self.capacity:
            self.cache.pop(next(iter(self.data.keys())))
        self.cache.update({key: value})

    def rem(self, key: str) -> None:
        if key in self.cache:
            self.cache.pop(key)

    def toString(self) -> String:
        return str(self.cache)