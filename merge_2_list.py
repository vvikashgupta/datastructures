#!/usr/local/bin/python

class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None

def merge2(l1 , l2):
    print l1 , l2
    if not l1: 
        return l2
    elif not l2:
        return l1
    elif l1.val < l2.val:
        merge2(l1.next , l2)
        return l1
    else:
        merge2(l1 , l2.next)
        return l2

def main():
    #create l1
    node1 , node2 , node3 = ListNode(1) , ListNode(2), ListNode(4)
    node1.next = node2 
    node2.next = node3
    l1 = node1
    node1 , node2 , node3 = ListNode(1) , ListNode(3), ListNode(4)
    node1.next = node2 
    node2.next = node3
    l2 = node1
    print merge2(l1 , l2)

if __name__ == '__main__':
    main()
