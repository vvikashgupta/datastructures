#!/usr/local/bin/python

def plusone(digits):
    
   # if digits[-1] != 9:
   #     result = [ x for x in digits]
   #     result[-1] += 1
   #     return result
    result = []
    carry = 1
    for digit in digits[::-1]:
        print digit
        if digit == 9 and carry == 1:
            print 
            digit = 0
            carry = 1
        elif carry == 1:
            digit += 1
            carry = 0
        else:
            pass
        result.append(digit)
        print result
    if carry:
        result.append(1)

    return result[::-1]
        
        
def main():
    print plusone([9])

if __name__ == '__main__':
    main() 
