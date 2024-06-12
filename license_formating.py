    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        import re
        str_to_work = re.sub(r'-','',S)
        st = str_to_work[::-1]
        index = 0
        result = ""
        while index <= len(st)-K-1:
            result += st[index:index+K] + '-'
            index += K
        result += st[index:]
        return result[::-1].upper()
