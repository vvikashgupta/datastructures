class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        index = 0
        print(costs)
        while coins and index <= len(costs)-1:
            print(f'{index}, {coins},{count}')
            if coins >= costs[index]:
                coins -= costs[index]
                count += 1
                index += 1
            else:
                return count
                break
        return count
