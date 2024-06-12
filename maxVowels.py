#!/usr/local/bin/python

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        print(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        max_vowels = 0
        s_len = len(s)
        def new_helper(st):
            from collections import Counter
            c = Counter(st)
            return c['a'] + c['e'] + c['i'] + c['o'] + c['u']

        def helper(st):
            count = 0
            nonlocal vowels
            for ch in st:
                if ch in vowels:
                    count += 1
            print(f'string is {st} , count is {count}')
            return count
        for index in range(s_len - k +1):
            max_vowels = max(max_vowels, new_helper(s[index:index+k]))
            if max_vowels == k:
                return k
        return max_vowels

def main():
    s = Solution()
    print(s.maxVowels("weallloveyou", 7))

if __name__ == '__main__':
    main()
