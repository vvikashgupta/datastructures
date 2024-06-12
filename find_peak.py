#!/usr/local/bin/python

#This solution is using binary search.
def find_peak(nums):
    print(nums)
    if not nums:
        return None
    l , r = 0 , len(nums)-1
    while l < r:
        m = (l + r )//2
        print( m , l , r)
        if nums[m] < nums[m+1]:
            l = m + 1
        else:
            r = m
        print( nums[m] , nums[m+1])
    return r


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lower = 0
        if len(nums) < 2:
            return 0
        elif len(nums) ==2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1
        else:
            pass
        for index , num in enumerate(nums):
            if index == 0:
                if num > nums[index+1]:
                    return index
                lower = num
            elif index == len(nums) -1:
                if num > lower:
                    return index
                return None
            elif lower < num > nums[index+1]:
                return index
            else:
                lower = num
        else:
            return None


def main():
    print( find_peak([1,2,3,1]))
    print(find_peak([1,2,1,3,5,6,4]))
    solu = Solution()
    print(solu.findPeakElement([1,2,3,1]))
    print(solu.findPeakElement([1,2,1,3,5,6,4]))

if __name__ == '__main__':
    main()
    
            
