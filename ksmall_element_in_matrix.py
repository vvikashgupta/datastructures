#!/usr/local/bin/python

import itertools as it
import heapq

def kth_smallest_element(matrix, k):
#    print(matrix)
#    lst = list(it.chain(matrix[0],matrix[1],matrix[2]))
#    print(lst)
    lst = heapq.merge(*matrix)
#    print(lst)
#    heapq.heapify(lst)
#    print(lst)
    print(heapq.nsmallest(k, lst))
#    print(ret_lst)
#    return ret_lst[-1]

def main():
   matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
   ]
   k = 5,
   print(kth_smallest_element(matrix , k))

if __name__ == '__main__':
    main()
