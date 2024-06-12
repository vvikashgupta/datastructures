#!/usr/local/bin/python


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

def validate_bst(tree):
    left_validated = right_validated = True
    if not tree:
        return True

    if tree.left:
        print(f' left tree value is {tree.left.value}')
        validate_bst(tree.left)
        if tree.left.value >= tree.value:
            print('Returning false')
            return False
            left_validated = False
    if tree.right:
        print(f' right tree value is {tree.right.value}')
        validate_bst(tree.right)
        if tree.right.value < tree.value:
            print('Returning false')
            return False
            right_validated = False
    #return left_validated and right_validated
    return True

def main():
    tree = TreeNode(2)
    tree.left = TreeNode(1)
    tree.right = TreeNode(3)
    print(validate_bst(tree))

if __name__ == '__main__':
    main()


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        from collections import deque
        que = deque()
        if not root:
            return True
        else:
            que.append(root)

        while que:
            node = que.pop()
            if not node:
                continue
            value = node.val
            if node.left:
                if node.left.val >= value:
                    return False
                que.append(node.left)
            if node.right:
                if node.right.val <= value:
                    return False
                que.append(node.right)
        return True 
