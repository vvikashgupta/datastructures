#!/usr/local/bin/python

def match(board,words):
    from collections import Counter , OrderedDict
    import itertools as it
    lst = it.chain(board)
    print( lst)
    word_count = Counter()
    for items in lst:
        new = Counter(items)
        word_count = word_count + new

    print( word_count)
    result_lst = []
    for word in words:
        for letters in word:
            if word_count[letters] <= 0 :
                break
        else:
            result_lst.append(word)
    return result_lst 

def main():
    board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
    words = ["oath","pea","eat","rain"]
    print( match(board , words))

if __name__ =='__main__':
    main()
