class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split(" ")
        result = ""
        vow = set(["a","e","i","o","u","A","E","I","O","U"])
        num_a = "a"
        for w in words:
            if w[0] in vow:
                result += w + "ma" + num_a
            else:
                result += w[1:] + w[0] + "ma" + num_a
            num_a += "a"
            result += " "
        return result.strip()
