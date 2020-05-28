class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        # Building a Graph
        
        dic = collections.defaultdict(list)
        for edges in dislikes:
            v1 = edges[0]
            v2 = edges[1]
            dic[v1].append(v2)
            dic[v2].append(v1)
        # Now the coloring ALGO
        
        queue = collections.deque()
        dicColor = {}

        for n in range(1, N+1):
            if n not in dicColor:
                queue.append(n)

                dicColor[n] = "B"

                while queue:
                    size = len(queue)
                    for i in range(size):
                        root = queue.popleft()

                        if dicColor[root] == "B":
                            color = "R"
                        else:
                            color = "B"
                        
                        for v in dic[root]:
                            if v in dicColor:
                                if dicColor[v] != color:
                                    return False                            
                            else:
                                dicColor[v] = color
                                queue.append(v)
                queue = collections.deque()
            # print(dicColor)
            # print(queue)
        return True
                    
