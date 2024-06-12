"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

You just dropped out of the connection.
"""

def say_hello():
    print('Hello, World')

def find_intersection(nums1, nums2):
    nums1_len = len(nums1)
    nums2_len = len(nums2)
    result = []
    for index in range(nums2_len):
        if nums2[index] in nums1:
            result.append(nums2[index])
            nums1.remove(nums2[index])
    return result

from collections import Counter
def better_intersection(nums1, nums2):
    c1 = Counter(nums1)
    c2 = Counter(nums2)
    result = []
    for key, value in c2.items():
        if key in c2:
            c1_value = c1[key]
            num_val = min(c1_value, value)
            for i in range(num_val):
                result.append(key)
    return result


def combine_array(nums1, nums2):
    left_index = right_index = len(nums2)-1
    
    while left_index >= 0  and right_index >= 0:
        if nums1[left_index] > nums2[right_index]:
            left_index -= 1
        else:
            nums1.pop()
            nums1.insert(left_index, nums2[right_index])
            right_index -= 1
            nums2.pop()

    while i, value in enumerate(nums2):
        nums1.pop()
        nums1.insert(i, nums2[i])
 
        
    
    

from collections import deque
def merge_array(nums1, nums2):
    index = 0
    for item in nums2:
        for index in range(len(index, nums1)):
            if item > nums1[index]:
                continue
            else:
                nums1.pop()
                nums1.insert(index, item)
                break

        
if __name__ == '__main__':
    #print(find_intersection([1,2,2,1], [2,2]))
    #print(find_intersection([4,9,5], [9,4,9,8,4]))
    
    #print(better_intersection([1,2,2,1], [2,2]))
    #print(better_intersection([4,9,5], [9,4,9,8,4]))
    list1 = [ 2, 3, 6, 8, 0, 0, 0, 0]
    list2 = [1, 1, 2, 3]
    #print(merge_array(list1, list2))
    #print(list1)
    print(combine_array(list1, list2))
    print(list1)
    
"""
Array A has N elements but has capacity 2*N (that is, only the first N slots have element), array B has N elements and capacity is also N. Both arrays are sorted and only contain integers. Write a function to merge B into A, in place. Result array should also be sorted.
Example:
A = [ 2, 3, 6, -, -, -], ## 6 slots, only first 3 slots have elements
B = [1, 2, 3]               ## 3 elements
return: A = [1, 2, 2, 3, 3, 6]  ## 6 elements, in place

C: 1, 2, 2, 3, 3, 6

"""
