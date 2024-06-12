#!?usr/local/bin/python

def minimumRefill(plants, capacityA, capacityB):
    plants_len = len(plants)
    a_index = 0 
    b_index = plants_len -1
    result = 0
    a_capacity = capacityA
    b_capacity = capacityB
        
    while True:
        print('while true')
        if a_capacity >= plants[a_index]:
            a_capacity -= plants[a_index]
        else:
            print(f' {a_capacity},{plants[a_index]}, {result}')
            result += 1
            a_capacity = capacityA
            a_capacity -= plants[a_index]
        if b_capacity >= plants[b_index]:
            b_capacity -= plants[b_index]
        else:
            print(f' {b_capacity},{plants[b_index]}, {result}')
            result += 1
            b_capacity = capacityB
            b_capacity -= plants[b_index]
        a_index += 1
        b_index -= 1
        if a_index >= b_index:
            break
    if a_index == b_index:
        if a_capacity < plants[a_index] and b_capacity < plants[a_index]:
            print(f'{a_capacity} {b_capacity},{plants[b_index]}, {result}')
            result += 1
    return result

if __name__ == '__main__':
   print(minimumRefill([1,2,4,4,5],6,5))
