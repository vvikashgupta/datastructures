#!/usr/local/bin/python

class Sum4:
    def __init__(self, nums):
        self.mem = {}
        self.nums = nums
        self.count = 0

    def find_combinations(self, target):
        self.count += 1
        if target in self.mem:
            print(f'target {target} found in mem')
            return self.mem[target]
        if not target:
            print(f'Target is null return 1')
            return 1
        ans = 0
        for num in self.nums:
            print(f'for loop num {num} for target {target}')
            if target - num >= 0:
                print(f' call find_combinations with target {target - num}')
                ans += self.find_combinations(target-num)
        self.mem[target] = ans
        print(f'return {self.mem[target]}')
        print(self.mem)
        print("====================")
        return self.mem[target]

def main():
    solution = Sum4([1,2,3,4,5])
    answer = solution.find_combinations(8)

if __name__ == '__main__':
    main()
