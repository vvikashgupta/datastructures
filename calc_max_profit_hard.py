#!/usr/local/bin/python

class stack:
    def __init__(self):
        self.lst = []

    def push(self, val):
        self.lst.append(val)

    def pop(self):
        if self.lst:
            return self.lst.pop()
       
    def is_empty(self):
        if not self.lst:
            return True
        else:
            return False 

    def printme(self):
        print(self.lst)

def cal_profit(start, end, profit):
    zipped = zip(start, end, profit)
    zipped = sorted(zipped, key:lambda element: element[0])
