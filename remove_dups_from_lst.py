#!/usr/local/bin/python

def remove_dups(nums):
    if len(nums) < 2: return len(nums)
    prev = nums[-1]
    for index in  range(len(nums) -2 , -1 ,-1) :
        print nums
        print "processing %d" %(index)
        if nums[index] == prev :
            nums.pop(index)
            print nums
        else:
            prev = nums[index]

    return len(nums)

def main():
    print remove_dups([1,1,2])
    print remove_dups([0,0,1,1,1,2,2,3,3,4])

if __name__ =='__main__':
    main()
