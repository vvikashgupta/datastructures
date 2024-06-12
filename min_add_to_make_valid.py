    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        bal = 0
        neg_balance = 0
        for chr in S:
            if chr == '(': bal +=1
            elif chr == ')':
                if bal == 0: neg_balance+=1
                else: bal -= 1
            else:
                pass
        print bal , neg_balance
        return bal + neg_balance
