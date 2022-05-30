class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if queryIP.find('.') != -1 and queryIP.find(':') != -1:
            return "Neither"
        if queryIP.find('.') != -1:
            queryIP_list = queryIP.split('.')
            if len(queryIP_list) != 4:
                return "Neither"
            for item in queryIP_list:
                if len(item) == 0 or len(item) > 3:
                    return "Neither"
                if len(item) > 1 and item[0] == '0':
                    return "Neither"
                if not item.isdigit():
                    return "Neither"
                if int(item) > 255 or int(item) < 0:
                    return "Neither"
            return "IPv4"
        if queryIP.find(':') != -1:
            queryIP_list = queryIP.split(':')
            if len(queryIP_list) != 8:
                return "Neither"
            for item in queryIP_list:
                if not 1 <= len(item) <= 4:
                    return "Neither"
                for c in item:
                    if not '0' <= c <= '9' and not 'a' <= c <= 'f' and not 'A' <= c <= 'F':
                        return "Neither"
            return "IPv6"
        return "Neither"