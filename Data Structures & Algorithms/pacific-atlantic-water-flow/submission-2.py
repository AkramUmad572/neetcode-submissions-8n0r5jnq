class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        flow = []
        pacific_visited, atlantic_visited = set(), set()

        def dfs(row, col, visited):
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr,dc in directions:
                dr, dc = dr + row, dc + col
                if dr in range(rows) and dc in range(cols) and ((dr, dc)) not in visited and heights[row][col] <= heights[dr][dc]:
                    visited.add((dr,dc))
                    dfs(dr, dc, visited)

        for i in range(max(rows, cols)):
            if i < cols:
                pacific_visited.add((0,i))
                dfs(0, i, pacific_visited)
            if i < rows:
                pacific_visited.add((i, 0))
                dfs(i, 0, pacific_visited)

        for n in range(max(rows, cols)):
            if n < rows:
                atlantic_visited.add((n, cols - 1))
                dfs(n, cols - 1, atlantic_visited)
            if n < cols:
                atlantic_visited.add((rows - 1, n))
                dfs(rows - 1, n, atlantic_visited)
            
        result = pacific_visited & atlantic_visited 
        return [[r,c] for r,c in result]


