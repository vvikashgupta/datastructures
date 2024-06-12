#!/usr/local/bin/python

class tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_sum(root,k):
        from collections import defaultdict
        result_dict = defaultdict(int)
        found = False
        if root:
            print " Check dictionary"
            def create_dict(root):
                if root and not found:
                    print "Check Next-node"
                    print result_dict
                    if k > root.val and result_dict[k - root.val] == 1:
                        found = True
                        result_dict[root.val] = 1
                        root = None
                        return None
                    result_dict[root.val] = 1
                    create_dict(root.left)
                    create_dict(root.right)                 
                else:
                    return None
        else:
            return found

def insert_data(root , node):
    if not root:
        return
    else:
        
def create_data(lst):
    root = None
    work-node = root
    for val in lst:
        node = tree(val)
        if not root:
            root = node
        else: 
            if val > root.value:
                root.left = node
            else:
                root.right = node
def main():
    
    find_sum(create_data([5,3,6,2,4,null,7],9)

if __name__ == '__main__':
    main()
