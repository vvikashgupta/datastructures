#!/usr/local/bin/python

class stack:
    def __init__(self):
        self.lst = []

    def push(self, value):
        self.lst.append(value)
    def pop(self):
        if self.lst:
            return self.lst.pop()
        else:
            return None

    def is_empty(self):
        return False if self.lst else True


def calculate(st):
    
def execute(str_num):
    st = stack()
    #Prepare the stack
         
   


def main():
    print(execute("20+3*2+5+10"))


if __name__ == '__main__':
    main()
