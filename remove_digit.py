#/use/local/bin/python3


def removeDigit(number, digit):
    result = []
    #number = [ n for n in number]
    
    if digit in number:
        count = number.count(digit)
        start = 0
        end = len(number)
        num = number
        while count:
            index = num.index(digit, start,end)
            start = index + 1
            num = num.pop(index)
            result.append(int(num))
            num = number
            count -= 1
        return max(num)

if __name__ == '__main__':
    print(removeDigit("123","3"))
