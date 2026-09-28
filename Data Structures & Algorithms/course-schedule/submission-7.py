class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for a,b in prerequisites:
            graph[a].append(b)

        path, safe = set(), set()

        def dfs(course: int) -> bool:
            if course in path:
                return False   
            if course in safe:
                return True

            path.add(course)

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            path.remove(course)
            safe.add(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True