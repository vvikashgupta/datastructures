#!/usr/local/bin/python

def check_valid(words):
    print(words)
    new_words = ["".join(lst) for lst in zip(*words)]
    print(new_words)
    return True if words == new_words else False

def main():
    words = [
  "abcd",
  "bnrt",
  "crmy",
  "dtye"
]
    print(check_valid(words))

if __name__ == '__main__':
    main()
