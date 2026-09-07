class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        visited = set()
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node, parent):
            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    pass
                elif nei in visited:
                    return False
                elif nei not in visited:
                    if not dfs(nei, node):
                        return False
            return True

        return dfs(0, None) and len(visited) == n

                    
                
            


