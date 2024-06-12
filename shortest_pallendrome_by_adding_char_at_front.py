class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def is_palindrome(s):
            return True if s == s[::-1] else False
        if not s and len(s) == 1:
            return s
        return_str = ""
        add_str = []
        if is_palindrome(s): return s
        for i in range(len(s)-1 , 0 , -1): # Reverse loop
            add_str.append(s[i])
            if is_palindrome(s[:i]):
                break
        return "".join(add_str) + s
