#/usr/local/bin/python

def check_number(N):
    print(N)
    result = 0
    num = str(N)
    str_len = len(num)
    for digit in str(N):
      print(f'result is {result} digit is {digit}')
      result += pow(int(digit) , str_len)
    print(f'{result}')
    if result == N:
        return True
    else:
        return False

def main():
    print(check_number(153))
    print(check_number(135))

if __name__ == '__main__':
    main()
