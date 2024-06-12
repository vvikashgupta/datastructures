#!/usr/local/bin/python

def 3sum(nums):
    import itertools as it
    num_iter = it.combinations(nums)
    result_set = []
    for item in num_iter:
        if sum(item) == 0 :
            sorted_items = sort(item)
            if sorted_items not in result_set:
                result_set.append(sorted_items)
    return result_set
                
            
