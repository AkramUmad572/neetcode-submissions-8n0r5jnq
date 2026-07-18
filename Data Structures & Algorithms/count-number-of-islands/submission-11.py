class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols =  len(grid), len(grid[0])
        islands = 0
        visit = set()


        def bfs(r,c):
            queue = collections.deque()
            queue.append((r,c))
            visit.add((r,c))

            while queue:
                row,col = queue.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr,dc in directions:
                    dr_row, dc_col = dr + row, dc + col
                    if dr_row in range(rows) and dc_col in range(cols) and grid[dr_row][dc_col] == "1" and ((dr_row, dc_col)) not in visit:
                        visit.add((dr_row, dc_col))
                        queue.append((dr_row, dc_col))        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and ((r,c)) not in visit:
                    bfs(r,c)
                    islands += 1
        return islands
