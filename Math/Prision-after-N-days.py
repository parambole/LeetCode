class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        
        seen = {}
        once = False
        while N > 0:
            curr = tuple(cells)
            # THis is cycle from that point onwards VVVVVV IMP
            if not once:
                if curr in seen:
                    # over here seen is greater
                    N = N % (seen[curr] - N)
                    once = True
                else:
                    seen[curr] = N
                
            if N > 0:
                N -= 1
                cells = self.shifting(cells)
        return cells
        
    def shifting(self, cells):
        res = []
        res.append(0)
        for i in range(1, len(cells) - 1):
            res.append(int(cells[i-1]==cells[i+1]))
        res.append(0)
        return res
