import re
class Solution:
    pat = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
    # It should begin with that pattern
    pattern_4 = re.compile(r'^(' + pat + r'\.){3}' + pat + r'$')
    
    pat = r'([0-9a-fA-F]{1,4})'
    pattern_6 = re.compile(r'^(' + pat + r'\:){7}' + pat + r'$')
    
    def validIPAddress(self, IP: str) -> str:        
        if self.pattern_4.match(IP):
            return "IPv4"
        return "IPv6" if self.pattern_6.match(IP) else "Neither"
