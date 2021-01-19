class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        
        # Step 1: Build the weighted Graph
        
        graph = collections.defaultdict(dict)
        
        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1.0 / val
            
        # Step 2: Finding the answer
        def dfs(x, y, visited):
            if x not in graph or y not in graph:
                return -1.0
            
            if y in graph[x]:
                return graph[x][y]
            
            else:
                for i in graph[x]:
                    if i not in visited:
                        visited.add(i)
                        temp = dfs(i, y, visited)
                        if temp == -1.0:
                            continue

                        return temp * graph[x][i]
                
            return -1.0
        
        res = []
        for query in queries:
            res.append(dfs(query[0], query[1], set()))
        return res
        
