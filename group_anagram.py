#!/usr/local/bin/python

def group_anagram(strs):
    from collections import defaultdict
    groups = defaultdict(list)
    output = []
    for lst in strs:
        key = "".join(sorted(lst))
        groups[key].append(lst)
    for key in groups.keys():
        output.append(groups[key])
    return output

def main():
    print( group_anagram(["eat","tea","tan","ate","nat","bat"]))

if __name__ == '__main__':
    main()
