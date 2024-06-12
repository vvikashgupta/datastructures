#!/usr/local/bin/python

def sum2(nums , i , j , k , result):
  #  print nums , i , j , k , result
    while i < j :
       adds = nums[i] + nums[j]
       if adds < k: # increment i
           i+= 1
       elif adds > k:
           j-= 1
       else:
           print nums[i] , nums[j] , -k
           result.add((nums[i] , nums[j] , -k))
           i+= 1
           j-=1
           while i < j and nums[i] == nums[i+1]:
               i+= 1
           while i < j and nums[j] == nums[j-1]:
               j-= 1

def sum3(nums):
    print nums
    result = set(tuple())
    nums.sort()
    print nums
    for k in range(2,len(nums)):
        sum2(nums , 0 , k-1 , -nums[k] , result)
    return result

def main():
    print sum3([-1, 0, 1, 2, -1, -4])
    print sum3([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])
    #print sum3([-12,4,12,-4,3,2,-3,14,-14,3,-12,-7,2,14,-11,3,-6,6,4,-2,-7,8,8,10,1,3,10,-9,8,5,11,3,-6,0,6,12,-13,-11,12,10,-1,-15,-12,-14,6,-15,-3,-14,6,8,-9,6,1,7,1,10,-5,-4,-14,-12,-14,4,-2,-5,-11,-10,-7,14,-6,12,1,8,4,5,1,-13,-3,5,10,10,-1,-13,1,-15,9,-13,2,11,-2,3,6,-9,14,-11,1,11,-6,1,10,3,-10,-4,-12,9,8,-3,12,12,-13,7,7,1,1,-7,-6,-13,-13,11,13,-8])

if __name__ == '__main__':
    main()
