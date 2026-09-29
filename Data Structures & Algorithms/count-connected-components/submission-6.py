class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen, connected = set(), 0
        graph = [[] for _ in range(n)]

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node: 'Node') -> int:
            if node in seen:
                return
            seen.add(node)

            for nei in graph[node]:
                dfs(nei)

        for edge in range(n):
            if edge not in seen:
                connected += 1
                dfs(edge)
                
        return connected
