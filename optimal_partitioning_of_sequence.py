class Solution:
    def partitionString(self, s: str) -> int:
        running_array = []
        result = 0
        slen = len(s)
        index = 0
        for i,v in enumerate(s):
            if v in running_array:
                result += 1
                running_array = [v]
            else:
                running_array.append(v)
        if running_array:
            result += 1
        return result
