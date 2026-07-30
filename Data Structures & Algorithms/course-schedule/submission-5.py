class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        visiting = set()
        graph = [[] for _ in range(numCourses)]
        
        for i in prerequisites:
            a = i[0]
            b = i[1]
            graph[b].append(a)

        def dfs(node):
            if node in visited:
                return True
            elif node in visiting:
                return False
            visiting.add(node)
            for preq in graph[node]:
                if not dfs(preq):
                    return False
            visiting.remove(node)
            visited.add(node)
            return True
        
        for cycle in range(numCourses):
            if not dfs(cycle):
                return False
        return True



