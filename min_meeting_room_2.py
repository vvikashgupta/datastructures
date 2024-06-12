class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        import heapq
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        rooms = []
        heapq.heappush(rooms, intervals[0][1])
        for item in intervals[1:]:
            if rooms[0] <= item[0]:
                # Pop out existing min and insert this new min.
                heapq.heappop(rooms)
                heapq.heappush(rooms, item[1])
            else:
                heapq.heappush(rooms, item[1])
        return len(rooms)
        
        '''
        import heapq
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        free_rooms = []
        heapq.heappush(free_rooms, intervals[0][1])
        for interval in intervals[1:]:
            if free_rooms[0] < interval[1]:
                heapq.heappop(free_rooms)
                
            heapq.heappush(free_rooms, interval[1])
        return len(free_rooms)
        ''' 
