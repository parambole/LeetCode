class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            n = len(row) - 1
            i = 0
            while i <= n / 2:
                row[i], row[n-i] = row[n-i] ^ 1, row[i] ^ 1
                i += 1
        return A
