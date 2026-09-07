class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited, counter = set(), 0

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
        
        for node in range(n):
            if node not in visited:
                counter += 1
                dfs(node)
        return counter
