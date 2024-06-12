#!/usr/local/bin/python

def longest_substring(s):
    from collections import deque
    longest_string = ""
    dobj = deque()
    print s
    for element in s:
        if element not in dobj:
            print "unique string append to dobj %s" %(dobj)
            dobj.append(element)
        else:
            print "duplicate found ...remove from left till current element is removed"
            if len(longest_string) < len(dobj):
                longest_string = "".join(dobj)
            for i in range(len(dobj)):
                                        
                check_element = dobj.popleft()
                print "poped element is %s" %(check_element)
                if check_element ==  element:
                    dobj.append(element)
                    break

        if not dobj:
            print "empty dobj append to dobj "
            dobj.append(element)
    llen = len(longest_string)
    dlen = len(dobj)
    if llen < dlen:
        return dlen
    else:
        return llen

def main():
   print  longest_substring("abcabcbb")
   print  longest_substring("bbbbb")
   print  longest_substring("pwwkew")

if __name__ == '__main__':
    main()
