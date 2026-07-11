class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0:
            return True

        graph = [[] for _ in range(numCourses)]
        visited, visiting = set(), set()

        for a,b in prerequisites:
            if a < 0 or a >= numCourses or b < 0 or b >= numCourses:
                return False
            graph[a].append(b)


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
            if not dfs(courses):
                return False
        return True

