class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gcount = scount = 0
        ans = 0
        while gcount < len(g) and scount < len(s):
            #print(f'{g[gcount]},{gcount}, {s[scount]},{scount}')
            if g[gcount] <= s[scount]:
                ans += 1
                gcount += 1
                scount += 1
                continue
            elif g[gcount] > s[scount]:
                scount += 1
                continue
            else:
                break
        return ans
