#!/usr/local/bin/python

def multiply(num1,num2):
    print( num1 , num2)
    def multiply_digits(a,b):
        return str(int(a) * int(b))

    def add_digits(a,b):
        return  str(int(a) + int(b)) 

    result_num = "0"
    if not num1 or not num2:
        return "0"
    for index ,num in enumerate(reversed(num1)):
        if index:
            result = multiply_digits(num , num2) + index * '0'
        else: 
            result = multiply_digits(num , num2)
        result_num = add_digits(result_num , result)
    return result_num
       

def main():
    print( multiply("2","3"))
    print( multiply("23","23"))

if __name__ == '__main__':
    main()
    
