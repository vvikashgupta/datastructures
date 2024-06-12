    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        import itertools as it
        from collections import OrderedDict
        import re
        dict = OrderedDict(int)
        for email in iter(emails):
            alst = email.split('@')
            if "." in alst[0]:
                newzero = re.sub(r'.','',alst[0])
                alst[0] = newzero
            if '+' in alst[0]:
                newlst = alst[0].split('+')
                alst[0] = newlst[0]
            email_to_append = "@".join(alst)
            if email_to_append not in dict:
                dict[email_to_append] = 1
        return len(dict.keys())
