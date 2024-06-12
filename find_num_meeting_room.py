#!/usr/local/bin/python

def minMeetingRooms(intervals):
    import heapq
    print(intervals)
    intervals.sort(key=lambda x: x[0])
    print(intervals)
    free_rooms = []
    heapq.heappush(free_rooms, intervals[0][1])
    print(free_rooms)
    for interval in intervals[1:]:
        print(interval)
        if free_rooms[0] < interval[1]:
            print(f'{free_rooms[0]} <= {interval[1]}')
            print(heapq.heappop(free_rooms))
               
        heapq.heappush(free_rooms, interval[1])
    print(free_rooms)
    return len(free_rooms)

def to_pointer_approach(intervals):
    if not intervals:
        return 0

    start_time = sorted([x[0] for x in intervals])
    end_time = sorted([x[1] for x in intervals])
    start_p, end_p = 0, 0
    meeting_req = len(intervals)
    room_required = 0
    while start_p < meeting_req:
        print(f'{start_p},{end_p},{start_time},{end_time} , {room_required}')
        if start_time[start_p] >= end_time[end_p]:
           room_required -= 1
           end_p += 1
        room_required += 1
        start_p += 1
    return room_required 

def main():
    print(minMeetingRooms([[0,30],[5,10],[15,20]]))
    print("============")
    print(minMeetingRooms([[7,10],[2,4]]))
    print("============")
    print(minMeetingRooms([[5,8],[6,8]]))
    print("============")
    print(to_pointer_approach([[0,30],[5,10],[15,20]]))
    print("============")
    print(to_pointer_approach([[7,10],[2,4]]))
    print("============")
    print(to_pointer_approach([[5,8],[6,8]]))
    

if __name__=='__main__':
    main()
