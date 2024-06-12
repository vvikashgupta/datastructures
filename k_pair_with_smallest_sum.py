class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        from heapq import heapify, heappop
        result = []
        heapify(nums1)
        heapify(nums2)
        count = 0
        n1 = heappop(nums1)
        n2 = heappop(nums2)
        result.append([min(n1,n2),max(n1,n2)])
        count += 1
        while count < k and nums1 and nums2:
            if heapq.nsmallest(1,nums1) >= heapq.nsmallest(1,nums2):
                n2 = heappop(nums2)
            else:
                n1 = heappop(nums1)
            result.append([min(n1,n2),max(n1,n2)])
            count += 1
        
        return result
