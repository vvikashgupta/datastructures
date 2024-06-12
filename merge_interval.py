#!/usr/local/bin/python

def merge_interval(intervals):
    print intervals
    intervals.sort(key=lambda x: x[0])
    print intervals
    class stack:
        def __init__(self):
            self.lst = []
        def push(self , value):
            self.lst.append(value)
        def pop(self):
            if self.lst:
                return self.lst.pop()
            else:
                return 0
        def printme(self):
            print self.lst
        def get_top(self):
            return self.lst[-1]
        def is_empty(self):
            if self.lst:
                return False
            else:
                return True
             
    st = stack()    
    for lst in iter(intervals):
        print lst
        print st.printme()
        if st.is_empty():
            print "empty stack case"
            st.push(lst[0])
            st.push(lst[1])
            print st.printme()
        else:
            print "Non-empty stack case"
            print lst
            print st.get_top()
            if st.get_top() < lst[0]: # Add lst items to the list
                print "lst is not included in stack. Add it"
                st.push(lst[0])
                st.push(lst[1])
            elif st.get_top() < lst[1]:
                print "lst is overlapping ...update top of the list"
                st.pop()
                st.push(lst[1])
            else:
                print "Nothing seems relevant"
                pass
    return_lst = []
    print "Processing done. let us divide stack into list"
    print st.printme()
    while not st.is_empty():
        val1 = st.pop()
        val2 = st.pop()
        return_lst.append([val2,val1])
    return return_lst[::-1]

def main():
    print merge_interval([[1,3],[2,6],[8,10],[15,18]])

if __name__ == '__main__':
    main()
