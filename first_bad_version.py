#!/usr/local/bin/python

def firstBad(n):
    if not n:
        return 0
    min_bad_version = 0
    max_bad_version = n
    while min_bad_version <= max_bad_version:
        if isBadVersion((min_bad_version + max_bad_version)/2):
            max_bad_version = (min_bad_version + max_bad_version)/2
        else:
            min_bad_version = (min_bad_version + max_bad_version)/2
    if min_bad_version == max_bad_version:
        return false
    else:
    	return min_bad_version
       

def main():
    print firstBad(5)

if __name__ == '__main__':
    main()
