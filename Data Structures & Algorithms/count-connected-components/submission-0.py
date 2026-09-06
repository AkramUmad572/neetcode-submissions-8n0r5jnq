class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited, connected = set(), 0 
        def dfs(node):
            for nei in adj[node]:
                if nei in visited:
                    pass
                else:
                    visited.add(nei)
                    dfs(nei)

        for node in range(n):
            if node in visited:
                pass
            else:
                dfs(node,)
                connected += 1

        return connected



