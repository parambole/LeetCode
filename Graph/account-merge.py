class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        # Email to name for later 
        
        em_to_name = {}
        
        # build the initial graph
        
        graph = collections.defaultdict(set)
        
        
        # So we have used a central node concept to connect
        """
         0
         /\
        """
        """
        So any one node can be connected to another component
        """
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                em_to_name[email] = name
                
        # This is imp for traversal
        seen = set()
        ans = []
        for email in graph:
            if email not in seen:
                seen.add(email)
                stack = [email]
                component = []
                
                # Standard DFS
                while stack:
                    node = stack.pop()
                    component.append(node)
                    # IMP to put only those neighbours that are not seen
                    for nei in graph[node]:
                        if nei not in seen:
                            # I have seen it now start exploring it
                            seen.add(nei)
                            stack.append(nei)
                ans.append([em_to_name[email]] + sorted(component))
                
        return ans
                    
            
        
                
                
            
        
