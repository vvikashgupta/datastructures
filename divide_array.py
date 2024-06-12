#!/usr/local/bin/python

def divide_array(lst):
    sum_of_left_num = 0
    print lst
    sum_of_right_num = 0
    lst_length = len(lst)
    index_left = 0
    index_right = lst_length -1
    if not lst:
        return -1
    else:
        while index_right >= index_left:
            if index_left == 0:
                sum_of_left_num += lst[index_left]
                sum_of_right_num += lst[index_right]
                index_left += 1
                index_right -= 1
                if sum_of_left_num == sum_of_right_num and index_left == index_right:
                    return index_left
         
            else:
                print "Non -zero scenario"
                print index_left , index_right , sum_of_left_num , sum_of_right_num
                if sum_of_left_num > sum_of_right_num:
                   print "Add right side to sum"
                   
                   sum_of_right_num += lst[index_right]
                   index_right -= 1
                elif sum_of_left_num < sum_of_right_num:
                    print "Add left side to sum"
                    sum_of_left_num += lst[index_left]
                    index_left += 1
                else:
                    print "left and right sums are equal"
                    if index_left == index_right: 
                        print "middle-index found with equal sum"
        		print "========"
                        return index_left 
                    else:
                        print "More elements are present in array. Continue"
                        sum_of_left_num += lst[index_left]
                	sum_of_right_num += lst[index_right]
                	index_left += 1
                	index_right -= 1
                        if sum_of_left_num == sum_of_right_num and index_left == index_right:
        		    print "========"
                            return index_left
        print "========"
        return -1
                     
                 
def main():
    print divide_array([1,3,5,10,5,4])
    print divide_array([4, 6, 9, 4, 3, 3, 3, 3, 3, 4])
    print divide_array([4, 8, 9, 4, 3, 6, 2])

if __name__ == '__main__':
    main()
                  
