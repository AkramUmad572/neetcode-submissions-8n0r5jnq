class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = [[] for _ in range(n)] 

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node: 'edge', parent: 'parent') -> bool:
            if node in visited:
                return False
            visited.add(node)

            for edge in graph[node]:
                if edge == parent:
                    continue
                if not dfs(edge, node):
                    return False
            return True
        
        dfs(0, None)
        return len(visited) == n 