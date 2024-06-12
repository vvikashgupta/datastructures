#!/usr/local/bin/python

def roman2Int(s):
    roman_dict = { 'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    if not s : return 0
    result = 0
    num , length = 0 , len(s) -1
    while num <= length:
        if num == length:
            result += roman_dict[s[num]]
            break  
        if roman_dict[s[num]] != roman_dict[s[num+1]] and roman_dict[s[num]] < roman_dict[s[num + 1]]:
            # The two numbers are lower-num
            result += roman_dict[s[num + 1]] - roman_dict[s[num]]
            num += 2
        else:
            result += roman_dict[s[num]]
            num += 1
    
    return result
       
def main():
    print roman2Int("III") 
    print roman2Int("LVIII") 
    print roman2Int("MCMXCIV") 
    print roman2Int("IX") 

if __name__ == '__main__':
    main()
