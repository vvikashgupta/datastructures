#!/usr/local/bin/python

class stack:
    def __init__(self):
        self.lst = []
        
    def push(self, num):
        self.lst.append(num)

    def pop(self):
        if self.lst:
            return self.lst.pop()
        else:
            None

    def is_not_empty(self):
        return True if self.lst else False

    def print_me(self):
        print(self.lst[::-1]

class Node:
    def __init__(self, value):
        self.num = value
        self.next = None

def create_stack(lst):
    st = stack()
    prev = lst
    while lst1:
        st.push(prev.num)
        prev = lst.next
        lst = lst.next
    return st


def add_2_lst(lst1, lst2):
    carry = 0
    result = stack()
    st1 , st2 = create_stack(lst1), create_stack(lst2)
    while st1.is_not_empty() or st2.is_not_empty():
        num1, num2 =  = st1.pop(), st2.pop()
        if num1 and num2:
             
            num = num1 + num2
        elif num1:
            num = num1
        else:
            num = num2
        
        if num > 9:
            carry = 1
