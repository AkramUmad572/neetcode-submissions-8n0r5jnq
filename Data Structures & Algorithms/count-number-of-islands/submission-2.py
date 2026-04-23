class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visit = set()

        def bfs(r, c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                distance = [[1,0], [-1,0], [0,1], [0,-1]]

                for dr, dc in distance:
                    dr_rows = row + dr
                    dr_cols = col + dc
                    if (dr_rows in range(rows) and dr_cols in range(cols) and grid[dr_rows][dr_cols] == "1" and (dr_rows, dr_cols) not in visit): 
                        q.append((dr_rows, dr_cols))
                        visit.add((dr_rows, dr_cols))




        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        return islands
