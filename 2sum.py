#!/usr/local/bin/python

def twosum(nums , target):
    dict = {}
    print(f'{nums}')
    for index , num in enumerate(nums):
        if target - num not in dict:
            print "if"
            dict[num] = index + 1
        else:
            print "in else"
            lst = [ dict[target-num] , index+1]
            return lst
        print dict


def main():
    print twosum([2,7,11,15],9)

if __name__ == '__main__':
    main()
