#!/usr/local/bin/python

"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""



class Solution:
    
    def check_sub_string(self, s, p):
        if '?' in p:
            for index in range(len(p)):
                if p[index] == '?':
                    continue
                elif p[index] == s[index]:
                    continue
                else:
                    return False
            return True, s[len(p):]
        else:
            if s.startswith(p):
                return True
            else:
                return False
            
    def is_check_str(self, s, p):
        print(f"is_check_str called {s}, {p}")
        if not p or not s:
            return True, s
        elif '?' not in p:
            pos = s.find(p)
            if pos != -1:
                s = s[(pos+ len(p)):]
                print("is_check_str return True")
                return True, s
            else:
                print("is_check_str return False")
                return False, None
        else:
            #Handle the case that the substring may contain the '?'
            s_index = p_index = 0
            found = False
            while s_index < len(s) and p_index < len(p):
                print(f'{s[s_index]}, {p[p_index]}')
                if s[s_index] != p[p_index]:
                    s_index += 1
                    if found:
                        if p[p_index] == '?':
                            p_index += 1
                        else:
                            return False, None
                else:
                    found = True
                    s_index += 1
                    p_index += 1
            return True, s[len(p):] 
        
        
        
    def isMatch(self, s: str, p: str) -> bool:
        print(f' s {s} p {p}')
        result = False
        if not s and not p:
            return True
        if not s or not p:
            return result
        
        if '*' in p:
            sub_str = p.split('*')
            print(sub_str)
            for st in sub_str:
                print("check is_check_str")
                status, s = self.is_check_str(s, st)
                if not status:
                    return False
            return True
                
        else:
            if len(s) != len(p):
                return False
            ret_value = self.check_sub_string(s, p)
            return ret_value


def main():
    s = Solution()
    print(s.isMatch("aa", "*"))
    print("===========")
    print(s.isMatch("ab", "?*"))
    print("===========")
    print(s.isMatch("abefcdgiescdfimde", "ab*cd?i*de"))


if __name__ == '__main__':
    main()
