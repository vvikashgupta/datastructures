#!/usr/local/bin/python


def letterCombinations( digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    phone = {'2': ['a', 'b', 'c'],
     '3': ['d', 'e', 'f'],
     '4': ['g', 'h', 'i'],
     '5': ['j', 'k', 'l'],
     '6': ['m', 'n', 'o'],
     '7': ['p', 'q', 'r', 's'],
     '8': ['t', 'u', 'v'],
     '9': ['w', 'x', 'y', 'z']}

    output_result = []
    def helpCombine( current , moredigit):
        print( current , moredigit)
        if not moredigit:
            print( "No more digits ...let us add it to result")
            output_result.append(current)
            return
        else:
            print( "more digit exist")
            for chr in phone[moredigit[0]]:
                print( "for loop for char")
                helpCombine(current+chr , moredigit[1:])

    if not digits:
        return []
    else:
        helpCombine("",digits)
        return output_result

def main():
   print( letterCombinations("26"))

if __name__ == '__main__':
    main()
