#!/usr/local/bin/python

class Solution:
    def findLeastNumOfUniqueInts(self, arr, k: int) -> int:
        print(arr)
        from collections import Counter
        c = Counter(arr)
        lst = c.most_common()
        print(lst)
        count = k
        for i in range(1, k+1):
            nums = lst.pop()
            count -= nums[1]
            print(lst)
            print(count)
            if count == 0:
                break
            elif count < 0:
                lst.append([nums[0],1])
            else:
                continue
        print(lst)
        return len(lst)

def main():
    s = Solution()
    print(s.findLeastNumOfUniqueInts([4,3,1,1,3,3,2],3))

if __name__ == '__main__':
    main()
