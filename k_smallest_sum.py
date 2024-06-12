#!/usr/local/bin/python

def k_pair(num1, num2, k):
    itr1 = iter(num1)
    itr2 = iter(num2)
    result = []
    for index in zip(itr1,itr2):
        if k:
            result.append([index])
            k -= 1
    return result

def main():
    print(k_pair([1,7,11,],[2,4,6],3))

if __name__ == '__main__':
    main()
        
