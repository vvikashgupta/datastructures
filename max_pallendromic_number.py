class Solution:
    def largestPalindromic(self, num: str) -> str:
        from collections import Counter, defaultdict
        c = Counter(num)
        result = []
        d = defaultdict(int)
        max_odd = -1
        odd_set = False
        #print(c)
        # Pls.note that we have only 10 digits.
        for k,v in c.items():
            d[k] = v
        #print(d)
        start = False
        for i in range(9,-1,-1):
            
            count = d[str(i)]
            #print(f'{count},{i}')
            if not odd_set and count % 2:
                max_odd = str(i)
                odd_set = True
            n = count //2
            if n >= 1:
                n = count //2
                if i == 0 and start:
                    result.append(str(i)*n)
                else:
                    result.append(str(i)*n)
                    start = False
        
        ret = result + [max_odd] + result[::-1]
        
        return str(int("".join(ret)))
