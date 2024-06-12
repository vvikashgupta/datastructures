#!/usr/local/bin/python

def merge_2_array(nums1 , m , nums2 , n):
    num1_count = 0
    num2_count = 0
    while num1_count < 3 and num2_count < n:
       if nums1[num1_count] >= nums2[num2_count]:
           nums1.insert(num1_count,nums2[num2_count])
           num2_count += 1
           num1_count += 1
       else:
           num1_count += 1
    if num2_count < n -1:
        for index in range(n  , num2_count , -1):
            nums1.insert(num1_count + num2_count , nums2[num2_count])
            num2_count += 1
    print nums1
    return None

def main():
    print merge_2_array([1,2,3,0,0,0] , 3 , [2,5,6] , 3)
   
if __name__ == '__main__':
    main()
