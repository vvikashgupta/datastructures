#!/usr/local/bin/python

from collections import Counter

def sort_by_char(s):
    col = Counter(s)
    char_len = len(col)
    result = ""
    for letter , count in col.most_common(char_len):
        result += letter * count
    return result

def main():
    print(sort_by_char("tree"))
    print(sort_by_char("Aabb"))

if __name__ == '__main__':
    main()

