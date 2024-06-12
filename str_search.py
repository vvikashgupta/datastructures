#!/usr/local/bin/python

class Solution:
    def maxNumOfSubstrings(self, s: str):
        result = []
        num_of_unique_char = set(s)
        print(num_of_unique_char)
        if len(s) == len(num_of_unique_char):
            print('Returning whole string')
            for c in num_of_unique_char:
                result.append(c)
            return result
        
        for c in num_of_unique_char:
            c_count = s.count(c)
            if c_count == 1:
                result.append(c)
                continue
            else:
                index = s.find(c)
                for i in range(1,c_count):
                    if c != s[index+i]:
                        break
                else:
                    result.append(c*c_count)
                    continue
        
        #Now let us check for whatever we got and check if we remove those occurence
        str_array = list(s)
        print(result , str_array)
        for item in result:
            print(item)
            while True:
                for i in item:
                    if i in str_array:
                        str_array.remove(i)
                    else:
                        break
                else:
                    break
        else:
            print(str_array)
            if "".join(str_array) in s:
                result.append("".join(str_array))
        
        if not result:
            result.append(s)
            
        return result

def main():
    s = Solution()
    #print(s.maxNumOfSubstrings("abbaccd"))
    print(s.maxNumOfSubstrings("abcdefghijklmnopqrstuvwxyz"))

if __name__ == '__main__':
    main()
