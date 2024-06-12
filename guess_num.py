# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        print(n)
        while low <= high:
            print('while')
            mid = (low + high)//2
            gnum = guess(mid)
            print(f'gnum is {gnum} {mid}')
            if gnum == 0:
                print(f'return mid {mid}')
                return mid
            elif gnum < 0:
                high = mid -1
            else:
                low = mid + 1
        print('Nothing to return hence returning -1')
        return -1
        
        
        
