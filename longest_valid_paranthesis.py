#!/usr/local/bin/python

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        print(f' longestValidParentheses {s}')
        long_para = ""
        long_len = 0
        from collections import deque
        found = False
        def is_valid(st):
            nonlocal found
            #print(f'is_valid {st}')
            if not st:
                return True, 0
            balance = 0
            for ch in st:
                if ch == '(':
                    balance += 1
                else:
                    if balance:
                        balance -= 1
                    else:
                       # print(f' is_valid return false {st}')
                        return False, 0
            if not balance:
                print(f' is_valid return True {st}')
                found = True
                return True, len(st)
            else:
                #print(f' is_valid return False {st}')
                return False, 0
            
        for i in range(len(s)):
            #print(f'i is {i}')
            for j in range(len(s),i-1,-1):
                #print(f'j is {j}')
                if j - 1 < long_len:
                    continue
                result, length = is_valid(s[i:j])
                long_len = max(long_len , length)
        return long_len

def main():
    s = Solution()
    #print(s.longestValidParentheses("(()"))
    print(s.longestValidParentheses(")(())))(())())"))

if __name__ == '__main__':
    main()
