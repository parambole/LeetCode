class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        # This is a graph problem. So in graph problem it's very important to first build the graph and only then do all the calculations on it
        
        # Lets build the graph
        
        tracker = set(range(1, N + 1))
        
        dic = collections.defaultdict(list)
        
        
        # Now we are storing all the in nodes
        
        for t in trust:
            
            if t[0] in tracker:
                tracker.remove(t[0])
            
            dic[t[1]].append(t[0])
            
        if len(tracker) == 0:
            return -1
        else:
            judge = tracker.pop()
            return judge if len(dic[judge]) == N - 1 else -1
