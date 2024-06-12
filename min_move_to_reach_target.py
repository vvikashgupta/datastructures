class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while target > 1:
            
            if target % 2:
                target -= 1
            else:
                if maxDoubles:
                    target = target // 2
                    maxDoubles -= 1
                else:
                    count += (target -1)
                    break
            count += 1
        return count
