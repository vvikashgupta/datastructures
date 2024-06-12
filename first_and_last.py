#!/usr/local/bin/python

def find_position(nums , target):
    result = [-1,-1]
    print(nums, target)
    if not nums:
        return result
    left = 0
    right = len(nums) - 1
    mid = (left + right)//2
    found = False
    while left < right:
        mid = (left + right)//2
        print(mid , left , right)
        print(nums[mid],nums[left],nums[right])
        if nums[mid] > target:
            right = mid
        elif nums[mid]< target:
            left = mid+1
        else: #Number found
            found = True
            break
    # Consider the case that number is not found.
    if not found:
        return result 
    print( left , right , mid)
    left = right = mid
    while right + 1 < len(nums) and nums[right+1] == target:
        right += 1
    while  0 <= left -1  and nums[left -1] == target:
        left -=  1
    return [left , right]

def new_method(nums, target):
    result = [-1, -1]
    lst_len = len(nums)
    if target in nums:
        result[0] = nums.index(target)
        result[1] = result[0] + nums.count(target) -1
    return result

def main():
    print( find_position([5,7,7,8,8,10] , 8))
    print( find_position([5,7,7,8,8,10] , 6))
    print( find_position([2,2] , 2))
    print("=========")
    print( new_method([5,7,7,8,8,10] , 8))
    print( new_method([5,7,7,8,8,10] , 6))
    print( new_method([2,2] , 2))

if __name__ == '__main__':
    main()

              
            
