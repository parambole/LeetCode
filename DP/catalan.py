class Solution:
    def numTrees(self, n: int) -> int:
        self.g = []
        self.g.append(1)
        self.g.append(1)
        
        for i in range(2, n+1):
            total = 0
            for j in range(1, i+1):
                total += self.getValueofF(j,i)
            self.g.append(total)
        return self.g[-1]
    
    def getValueofF(self,i,n):
        return self.g[i-1] * self.g[n-i]
