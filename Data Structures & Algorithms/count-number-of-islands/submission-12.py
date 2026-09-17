from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited, islands = set(), 0


        def bfs(r,c):
            queue = deque()
            visited.add((r, c))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            queue.append((r,c))


            while queue:
                row, col = queue.popleft() 
                visited.add((row,col))
                
                for dr,dc in directions:
                    dr_rows, dc_cols = dr + row, dc + col
                    if dr_rows in range(rows) and dc_cols in range(cols) and ((dr_rows, dc_cols)) not in visited and grid[dr_rows][dc_cols] == "1":
                        visited.add((dr_rows, dc_cols))
                        queue.append((dr_rows, dc_cols))

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and ((r,c)) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands

        