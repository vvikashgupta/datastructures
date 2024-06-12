class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        result = []
        if finalSum % 2:
            return result
        incr = 2
        while incr <= finalSum:
            #print(f'{result},{incr},{finalSum}')
            result.append(incr)
            finalSum -= incr
            incr += 2
        #print(result)
        #print(finalSum)
        result[-1] += finalSum
        return result
