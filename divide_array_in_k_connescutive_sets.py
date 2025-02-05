
"""
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into sets of k consecutive numbers
Return True if its possible otherwise return False.

 

Example 1:

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
Example 2:

Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
Example 3:

Input: nums = [3,3,2,2,1,1], k = 3
Output: true
Example 4:

Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= nums.length
"""


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        result = False
        sub_array = []
        if not nums:
            return result
        if len(nums) < k:
            return result
        
        nums.sort()
        first_num = nums[0]
        count = 0
        while nums:
            tmp_array = []
            first_num = nums[0]
            sub_array.append([first_num])
            for i in range(k):
                if first_num + i in nums:
                    nums.remove(first_num + i)
                    tmp_array.append(first_num + i)
                else:
                    return False
            sub_array.append(tmp_array)
        return True
                    
