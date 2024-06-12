#!/usr/local/bin/python


class TreeNode(object):
    def __init__(self , value):
        self.val = value
        self.left = None
        self.right = None
def averageLevel(root):
    from collections import defaultdict , deque
    if not root:
        return 0
    levels = defaultdict(list)
    sum_list = []
    queue = deque([root,1])
    level = 0 
    while queue:
        node , level = queue.popleft()
        levels[level].append(node.val)
        if node.left:
            queue.append([node.left , level+1])
        if node.right:
            queue.append([node.right , level + 1])
    for k , v in levels.iteritems():
        sum_list.append(float(sum(v))/float(len(v)))
    return sum_list  

        
