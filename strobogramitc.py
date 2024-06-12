#!/usr/local/bin/python

def isstrobogramitc(num):
    if num:
        vlen = len(num) -1
        for index , value in enumerate(num):
            if value in "8":
                pass
            elif value == "1":
                    if num[vlen-index] == '1':
                        pass
                    else:
                        return False
            elif value == "0":
                    if num[vlen-index] == '0':
                        pass
                    else:
                        return False
            
            elif value == "6":
                    if num[vlen-index] == '9':
                        pass
                    else:
                        return False
            elif value == "9":
                    if num[vlen-index] == '6':
                        pass
                    else:
                        return False
            else:
                return False
        return True

def main():
    isstrobogramitc("69")

if __name__ == '__main__':
    main()
