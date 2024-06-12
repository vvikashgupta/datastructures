
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        result = []
        l = l1
        while l:
            result.append(l.val)
            l = l.next
        l = l2   
        while l:
            result.append(l.val)
            l = l.next
        
        result.sort()
        head_node = start_node = None
        for index , val in enumerate(result):
            if not start_node:
                start_node = ListNode(val, start_node)
                head_node = start_node
            else:
                start_node = ListNode(val, start_node)
        return head_node

def main()
