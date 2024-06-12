#!/usr/local/bin/python
import re

def check_string(base_string, match_string):
    if match_string and '#' in match_string:
        match_string = re.sub(r'#','',match_string)
    if not base_string:
        return False, base_string
    if not match_string:
        return True, base_string
    #if base_string == match_string:
    #    return True, None
    location = base_string.find(match_string)
    #print(f'check_string {base_string} , {match_string} {location}')
    if location != -1:
        return True, base_string[location:]
    else:
        return False, base_string
    

def check_pattern(base_string, match_pattern):
    
    print(f' check_pattern {base_string}, {match_pattern}')
    str_to_match = match_pattern.split('+')
    base = base_string
    print(f'{base_string} {str_to_match}')
    for str in str_to_match:
        #print(f' for loop {base} {str}')
        status, base = check_string(base, str)
        if not status:
            return False
    else:
        return True
   
def main():
    print(check_pattern("scoop","scoop")) 
    print("=================")
    print(check_pattern("scoop","s+op")) 
    print("=================")
    print(check_pattern("scoop","scOop")) 
    print("=================")
    print(check_pattern("scoop","sco#")) 
    print("=================")
    print(check_pattern("scoop","s+o+p")) 
    print("=================")
    print(check_pattern("scoop","scoop")) 
    print(check_pattern("scoop","s+++op")) 
    print(check_pattern("scoop","sc+o+p#")) 

if __name__ == '__main__':
    main()
