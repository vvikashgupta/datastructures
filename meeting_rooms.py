#!/usr/local/bin/python

def find_meeting_rooms(intervals):
    intervals.sort(key=lambda lst: lst[0])
    class stack:
        def __init__(self):
            self.lst = []
        def push(self,val):
            self.lst.append(val)
        def pop(self):
            if self.lst:
                return self.lst.pop()
            else:
                return None
        def get_top(self):
            if self.lst:
                return self.lst[-1]
            else:
                return None
        def is_empty(self):
            if self.lst:
                return True
            else:
                return False
    st = stack()
    result = 0
    meeting_rooms = 0
    current_rooms = 0
    for item in iter(intervals):
        print meeting_rooms , result , item
        if st.is_empty():
            print "isst entry on the stack"
            st.push(item[0])
            st.push(item[1])
            meeting_rooms = 1
            result = max(meeting_rooms , result)
        elif st.get_top() < item[0]:
            print "lst is greater than stack-top"
            # Non-overlapping meetings
            st.push(item[0])
            st.push(item[1])
            meeting_rooms = 1
            current_rooms = 1
            result = max(meeting_rooms , result)
        elif st.get_top() > item[1]:
            print "complet overlap"
            meeting_rooms += 1
            result = max(meeting_rooms , result)
        else:
            print "nothing important"
            meeting_rooms += 1
            result = max(meeting_rooms , result)
            st.pop()
            st.push(item[1])
    return result 

def main():
    print find_meeting_rooms([[0,30],[5,10],[15,20]])

if __name__ == '__main__':
    main()   
