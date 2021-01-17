class GNode(object):
    def __init__(self):
        self.inDegrees = 0
        self.outNodes = []

class Solution:

    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        from collections import defaultdict, deque
        # key: index of node; value: GNode
        graph = defaultdict(GNode)

        totalDeps = 0
        for relation in relations:
            nextCourse, prevCourse = relation[1], relation[0]
            graph[prevCourse].outNodes.append(nextCourse)
            graph[nextCourse].inDegrees += 1
            totalDeps += 1

        nodepCourses = deque()
        for index, node in graph.items():
            if node.inDegrees == 0:
                nodepCourses.append(index)

        removedEdges = 0
        minSememster = 0
        while nodepCourses:            
            k = 0
            n = len(nodepCourses)
            while k < n:
                course = nodepCourses.popleft()

                for nextCourse in graph[course].outNodes:
                    graph[nextCourse].inDegrees -= 1
                    removedEdges += 1
                    if graph[nextCourse].inDegrees == 0:
                        nodepCourses.append(nextCourse)
                k += 1
                    
            minSememster += 1

        if removedEdges == totalDeps:
            return minSememster
        else:
            return -1
