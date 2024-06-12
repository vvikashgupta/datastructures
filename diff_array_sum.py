#!/usr/local/bin/python

'''
def subArrayRanges(nums):
    result = 0
    nums_len = len(nums) 
    count = 0
    print(nums_len)
    for i in range(1, nums_len):
        print('inside for')
        if not i :
            continue
        else:
            print(f'process for {i}')
            for j in range(nums_len - i):
                print(nums[j:j+i+1])
                min_num = min(nums[j:j+i+1])
                max_num = max(nums[j:j+i+1])
                result += max_num - min_num
                
		print(result)
    return result
'''
def subArrayRanges(nums):
    result = 0
    nums_len = len(nums) 
    count = 0
    for i in range(1, nums_len):
        if not i :
            continue
        else:

            for j in range(nums_len - i):
                if j == 0:
                    initial_array = nums[0:i+1]
                    int_min = min(initial_array)
                    int_max = max(initial_array)
                else:
                    new_num = nums[j+i]
                    #print(f' {int_min} { 
                    if ( new_num < int_min or new_num > int_max ) or (int_min == nums[j] or int_max == nums[j]):
                        initial_array = nums[j:j+i+1]
                        int_min = min(initial_array)
                        int_max = max(initial_array)
                print(initial_array)
                result += int_max - int_min
                print(result)
    return result
if __name__ == '__main__':
    print(subArrayRanges([-69,-70,-56,-83,63]))
    print(subArrayRanges([-72,-68,57,-14,-50,71,-6,-20]))
