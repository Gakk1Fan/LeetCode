class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emails_set = set()
        res = 0
        for email in emails:
            a = email.split('@')[0]
            b = email.split('@')[1]
            c = a.split('+')[0].replace('.', '') + '@' + b
            # print(c)
            if c not in emails_set:
                res += 1
                emails_set.add(c)
        return res