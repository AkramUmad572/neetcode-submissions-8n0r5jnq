class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visted = set()
        islands = 0

        def bfs(r,c):
            queue = collections.deque()
            visted.add((r, c))
            queue.append((r,c))

            while queue:
                row, col = queue.popleft()
                directions = [(1,0), (0,1), (0,-1), (-1, 0)]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visted):
                        queue.append((r,c))
                        visted.add((r,c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visted:
                    bfs(r, c)
                    islands += 1
        return islands