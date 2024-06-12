#!/usr/local/bin/python

def max_profit(prices):
    print prices
    
    if not prices:
        return 0
    sell_price = [0 , prices[0]]
    max_price = [0, prices[0]]
    profit = 0
    for index , item in enumerate(prices):
        print "process entries %d %d" %(index , item)
        if sell_price[1] > item:
            print "process lower buy_price"
            sell_price[1] = item
            sell_price[0] = index
            max_price[1] = item
            max_price[0] = index
        if max_price[1] < item and max_price[0] < index:
            print "process higher sell_price"
            profit = max(profit,item - sell_price[1])
            max_price[1] = item
            max_price[0] = index
        print profit
    return profit

def main():
    print max_profit([7,1,5,3,6,4])
    print max_profit([7,6,4,3,1])

if __name__ == '__main__':
    main()
