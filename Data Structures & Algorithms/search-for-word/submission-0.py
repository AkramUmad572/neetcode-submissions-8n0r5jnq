class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, col = len(board), len(board[0])

        def dfs(r, c, k):
            #bounds mismatch
            if r < 0 or c < 0 or r >= rows or c >= col:
                return False
            
            #wrong character
            if board[r][c] != word[k]:
                return False
            
            #found full word
            if k == len(word) - 1:
                return True

            temp = board[r][c]
            board[r][c] = "#"

            #go all four directions
            found = (
                dfs(r + 1, c, k + 1) or
                dfs(r - 1, c, k + 1) or
                dfs(r, c + 1, k + 1) or
                dfs(r, c - 1, k + 1)
            )

            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
        return False


