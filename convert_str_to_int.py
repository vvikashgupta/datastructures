#!/usr/local/bin/python

def atoi(str):
    valid_array = ['1','2','3','4','5','6','7','8','9','0']
    sign = "-"
    st = str.strip()
    if not st: return 0
    count  , length = 0 , len(st) 
    convert_str = ""
    while count < length:
        if count == 0 and st[count] == '-':
            convert_str = '-'
            count += 1
            continue
        if st[count] in valid_array:       
           convert_str = convert_str + st[count]
           count += 1
        else:
            if not count or convert_str == '-':
                return 0
            else:
                return int(convert_str)
    if count == length and convert_str != '-':
        return int(convert_str)
    else:
        return 0


def main():
    print( atoi(" -42"))
    print( atoi(" -42 world"))
    print( atoi(" hello world"))
    print( atoi(" -293042493748872384394793087 w"))
    print( atoi('-'))
    print( atoi('0-1'))
    print( atoi('-+1'))

if __name__ == '__main__':
    main()
  
           
