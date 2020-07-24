class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        destination = len(graph)
        self.result = []
        self.dfs(graph, [0], 0, destination)
        return self.result
        
    def dfs(self, graph, path, curr, destination):
        if curr == destination - 1:
            self.result.append(path)
            return
            
        for i in graph[curr]:
            self.dfs(graph,path + [i],i,destination)
