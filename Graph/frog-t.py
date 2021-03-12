class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        
        g = [[] for i in range(n)]
        
        for i, j in edges:
            g[i - 1].append(j - 1)
            g[j - 1].append(i - 1)
                        
        visited = [False] * (n)
        prob = [0] * (n)
        prob[0] = 1
        
        queue = collections.deque([0])
        visited[0] = True
            
                
        while queue and t > 0:
            for _ in range(len(queue)):
                number_of_unvisted_vertex = 0
                node = queue.popleft()
                for v in g[node]: 
                    if not visited[v]: 
                        number_of_unvisted_vertex += 1
                for vertex in g[node]:
                    if not visited[vertex]:
                        queue.append(vertex)
                        visited[vertex] = True
                        prob[vertex] = prob[node] * 1 / number_of_unvisted_vertex
                
                if number_of_unvisted_vertex > 0: prob[node] = 0
                        
            t -= 1
                    
                    
        return prob[target - 1]
