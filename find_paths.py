#!/usr/local/bin/python




class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

paths = []
tmp_path = []

def find_paths(root, current_path, length):
    global paths
    print(root)
    print(current_path)
    if not root:
        return
    if not current_path:
        current_path.append(root.val)
    if len(current_path) > length:
        current_path[length -1 ] = root.val
    else:
        current_path.append(root.val)

    length += 1
    if not root.left and not root.right:
        lst = [x for x in current_path] 
        paths.extend([lst])
        
        print(f' append {current_path}')
        print(f' now paths is {paths}')
    
    find_paths(root.left, current_path, length)
    find_paths(root.right, current_path, length)


def main():

    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(1)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(1)
    root.right.right = TreeNode(1)
    find_paths(root, tmp_path, 0)
    print(paths)

if __name__ == '__main__':
    main()
