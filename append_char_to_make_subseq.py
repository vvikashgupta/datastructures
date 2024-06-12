class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        slen = len(s)
        tlen = len(t)
        sindex = tindex = 0
        #print(f'{slen},{tlen}')
        while sindex < slen and tindex < tlen:
            if s[sindex] == t[tindex]:
                #print('found a matching char')
                sindex += 1
                tindex += 1
                continue
            else:
                #print(' No matching char increase sequence')
                sindex += 1
        #print(f'{tindex}')
        return tlen - tindex
