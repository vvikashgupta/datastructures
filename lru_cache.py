from collections import deque, defaultdict
class LRUCache:

    def __init__(self, capacity: int):
        self.dict = defaultdict()
        self.deq = deque()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.dict:
            self.deq.remove(key)
            self.deq.append(key)
            return self.dict[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.deq.remove(key)
            self.deq.append(key)
            self.dict[key] = value
        else:
            self.dict[key] = value
            if len(self.deq) == self.capacity:
                remove_key = self.deq.popleft()
                del self.dict[remove_key]
            self.deq.append(key)
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
