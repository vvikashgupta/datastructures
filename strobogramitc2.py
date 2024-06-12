#!/usr/local/bin/python

def strobo(n):
    lst = [ '0','1','6','8','9']
    result_lst = []
    def is_strobogamitic(num):
        if num:
            vlen = len(num) -1
            for index , value in enumerate(num):
                if value in "8":
                    pass
                elif value == "1":
                        if num[vlen-index] == '1':
                            pass
                        else:
                            return False
                elif value == "0":
                        if num[vlen-index] == '0':
                            pass
                        else:
                            return False
                
                elif value == "6":
                        if num[vlen-index] == '9':
                            pass
                        else:
                            return False
                elif value == "9":
                        if num[vlen-index] == '6':
                            pass
                        else:
                            return False
                else:
                    return False
            return True
    import itertools as it
    #numlst_iter = it.combinations_with_replacement(lst , n)
    numlst_iter = it.product(lst , repeat=n)
    print numlst_iter
    for n in numlst_iter:
        print n
        num = "".join(n) 
        if is_strobogamitic(num) and int(num):
            result_lst.append(num)
    return result_lst

def main():
    print strobo(2)
    print strobo(3)
   # print strobo(4)

if __name__ == '__main__':
    main()
