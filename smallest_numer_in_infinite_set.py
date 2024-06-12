class SmallestInfiniteSet:

    def __init__(self):
        from heapq import heapify, heappop,heappush
        self.numset = set()
        self.current = 1
        self.heap = []
        heapify(self.heap)
        

    def popSmallest(self) -> int:
        if self.heap:
            ans = heappop(self.heap)
        else:
            ans = self.current
            self.current += 1
        return ans
    
        

    def addBack(self, num: int) -> None:
        if num >= self.current or num in self.heap:
            return
        heappush(self.heap, num)
        return
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
