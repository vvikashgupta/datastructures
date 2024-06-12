class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        no_of_use = [0]*n
        meetings.sort(key=lambda x: x[0])
        from heapq import heapify, heappop, heappush
        rooms = [i for i in range(n)]
        heapify(rooms)
        meeting_end = []
        heapify(meeting_end)
        remaining_meetings = []
        for meeting in meetings:
            print(meeting)
            if rooms:
                print('empty room')
                room = heappop(rooms)
                heappush(meeting_end, [meeting[1],room])
                no_of_use[room] += 1
                print(meeting_end)
            else:
                print('non empty room')
                end_time, room = heappop(meeting_end)
                heappush(meeting_end,[end_time + meeting[1],room])
                no_of_use[room] += 1
                print(meeting_end)
        print(no_of_use)
        return no_of_use.index(max(no_of_use))
            
