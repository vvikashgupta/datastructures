#!/usr/local/bin/python

def maxRotateFunction(A):
    from collections import deque
    que = deque(A)
    result = []
    for index in range(len(A)):
        result.append(sum([index*value for index,value in enumerate(que)]))
        que.rotate()
    print(result)
    return max(result)

def main():
    print(maxRotateFunction([4, 3, 2, 6]))

if __name__ == '__main__':
    main()
