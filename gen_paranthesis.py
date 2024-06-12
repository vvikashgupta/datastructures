#!/usr/local/bin/python

def generateParenthesis( n):
    ans = []
    def isValid(S):
        bal = 0
        for c in S:
            if c in "(" : bal += 1

            else:
                if bal == 0:
                    return False
                bal -= 1
        return bal == 0

    def backtrack( S = "", left = 0 , right = 0):
        print S,left , right
        if len(S) == 2*n:
            if isValid(S):
                print "Valid paranthesis %s" %(S)
                ans.append(S)
        if left < n:
            print "Add to the left"
            backtrack(S+"(",left +1 , right)
        if right < n:
            print "Add to the left"
            backtrack(S+")",left  , right + 1)
    backtrack()
    return ans

def main():
    print generateParenthesis(3)
 

if __name__ == '__main__':
    main()
