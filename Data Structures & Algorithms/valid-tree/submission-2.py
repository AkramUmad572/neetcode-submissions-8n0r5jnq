class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        def dfs(node, parent, graph, visited):
            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    pass
                elif nei in visited:
                    return False
                else:
                    if not dfs(nei, node, graph, visited) :
                        return False
            return True

        return dfs(0, -1, adj, visited) and len(visited) == n
