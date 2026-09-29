class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        graph = [[] for _ in range(n)]

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node: 'Node', parent: None) -> bool:
            if node in visited:
                return False
            visited.add(node)
 
            for nei in graph[node]:
                if nei in visited and nei != parent:
                    return False 
                elif nei == parent:
                    pass
                else:
                    if not dfs(nei, node):
                        return False
            return True
            
            
        return dfs(0, None) and len(visited) == n
