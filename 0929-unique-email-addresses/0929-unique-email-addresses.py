class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        mails = set()
        for email in emails:
            body = ""
            company = ""
            i = 0
            while email[i] != "@" and email[i] != "+":
                if email[i] != ".":
                    body += email[i]
                i += 1
            if email[i] == "+":
                while email[i] != "@":
                    i += 1
            i +=1
            while i < len(email):
                company += email[i]
                i += 1
            final_mail = body + "@" + company
            mails.add(final_mail)
        return len(mails)

        

                




        