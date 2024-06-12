#!/usr/local/bin/python
import heapq

def high_five(items):
    from collections import defaultdict
    import math
    result = []
    dict = defaultdict(list)
    for lst in items:
        dict[lst[0]].append(lst[1])
    for k ,v in dict.iteritems():
        print k , v
        vlan = len(v)
        if vlan > 5:
                v.sort() 
        	result.append([k,sum(v[vlen-5:vlan-1])/5
        else:
        	result.append([k , sum(v)/len(v)])
    print result
    return result

def main():
    high_five([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]])

if __name__ == '__main__':
    main()
