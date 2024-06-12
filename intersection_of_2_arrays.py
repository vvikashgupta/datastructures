#!/usr/local/bin/python

def intersect_array(nums1 , nums2):
    #print nums1 , nums2
    if not nums1 or not nums2:
        return []
    result = []
    for num in nums2:
        if num in nums1:
            result.append(nums1.pop(nums1.index(num)))
            if not nums1:
                return result
    return result

def main():
    print( intersect_array([1,2,2,1] , [2,2]))
    print( intersect_array([4,9,5] , [9,4,9,8,4]))

if __name__ == '__main__':
    main()
