class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        visiting = set()

        graph = [ [] for _ in range(numCourses)]

        for pair in prerequisites:
            a = pair[0]
            b = pair[1]
            graph[b].append(a)

        def dfs(node):
            if node in visiting:
                return True
            elif node in visited:
                return False
            visiting.add(node)
            for nei in graph[node]:
                if dfs(nei) == True:
                    return True
            visiting.remove(node)
            visited.add(node)
            return False

        for course in range(numCourses):
            if dfs(course):
                return False
        return True
