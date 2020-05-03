class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        freq = [0] * 26
        
        for c in magazine:
            idx = ord(c) - ord('a')
            freq[idx] += 1
        
        for c in ransomNote:
            idx = ord(c) - ord('a')
            if freq[idx] == 0:
                return False
            else:
                freq[idx] -= 1
        return True
