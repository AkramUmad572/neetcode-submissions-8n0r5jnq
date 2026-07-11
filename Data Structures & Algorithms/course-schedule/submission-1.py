class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0:
            return True
        for a,b in prerequisites:
            if a < 0 or a >= numCourses or b < 0 or b >= numCourses:
                return False
        
        graph = [[] for _ in range(numCourses)]
        for a,b in prerequisites:
            graph[a].append(b)

        visited, visiting = set(), set()

        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            visiting.add(node)
            
            for prereq in graph[node]:
                if not dfs(prereq):
                    return False
                
            visiting.remove(node)
            visited.add(node)
            return True
        
        for courses in range(numCourses):
            if courses not in visited:
                if not dfs(courses):
                    return False
        return True

