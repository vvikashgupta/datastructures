class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        nsum = sum(nums)
        index = 0
        print(nums)
        negative = False
        last_negative = 0
        count = 0
        while count < k and count < len(nums):
            print(f'{k}')
            if nums[index] > 0:
                print('inside ifmodifying either {nums[index]} or {nums[last_negative]} ')
                if k % 2:
                    if negative and abs(nums[last_negative]) <= nums[index]:
                        nums[last_negative] = -nums[last_negative]
                    else:
                        nums[index] = -nums[index]
                        print(f'change {nums[index]}')
                break
            elif nums[index] < 0:
                negative = True
                print(f'inside else modifying {nums[index]}')
                nums[index] = -nums[index]
                last_negative = index
                index += 1
                count += 1
                 
            else:
                break
        print(nums)
        return sum(nums)
