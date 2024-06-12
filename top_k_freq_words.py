class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        from heapq import heapify, heappop, heappush
        c = Counter(words)
        common_words = c.most_common()
        heap = [(-freq, word) for word,freq in c.items()]
        heapify(heap)
        result = [heappop(heap)[1] for _ in range(k)]
        print(result)
        
        return result
