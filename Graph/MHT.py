class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [ i for i in range(n)]
        
        remaining_nodes = n
        # we are not using a dic because they are all numnbers
        neighbours = [set() for i in range(n)]
        
        # Create the adj list
        for start, end in edges:
            neighbours[start].add(end)
            neighbours[end].add(start)
                    
        leaves = []
        for i in range(n):
            if len(neighbours[i]) == 1:
                leaves.append(i)
                
        # The assumption is that there can be more than 2 centroids
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            
            # The thing is at every round we just want to process the new leaves
            new_leaves = []
            
            while leaves:
                leaf = leaves.pop()
                # So iterate over all of its neighbours and find new leaves
                for neighbour in neighbours[leaf]:
                    neighbours[neighbour].remove(leaf)
                    if len(neighbours[neighbour]) == 1:
                        new_leaves.append(neighbour)
                        
            leaves = new_leaves
            
        return leaves
