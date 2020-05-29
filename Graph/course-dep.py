# When ever we need to store more properties then to this way

class Gnode:
    def __init__(self):
        self.inDegree = 0
        self.outNode = []

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(Gnode)
        
        total = 0
        
        for relation in prerequisites:
            nextC, prevC =  relation[0], relation[1]
            graph[prevC].outNode.append(nextC)
            graph[nextC].inDegree += 1
            total += 1
            
        noDep = collections.deque()
        
        for index, node in graph.items():
            if node.inDegree == 0:
                noDep.append(index)
                
        removed = 0
        while noDep:
            
            course = noDep.pop()
            
            for nextCourse in graph[course].outNode:
                graph[nextCourse].inDegree -= 1
                removed += 1
                
                if graph[nextCourse].inDegree == 0:
                    noDep.append(nextCourse)
                    
        if removed == total:
            return True
        

        return False
