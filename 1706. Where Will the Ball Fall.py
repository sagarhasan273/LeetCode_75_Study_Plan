class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r == rows-1:
                if grid[r][c] == 1 and c+1 < cols and grid[r][c] == grid[r][c+1]:
                    return c + grid[r][c]
                if grid[r][c] == -1 and c-1 > -1 and grid[r][c] == grid[r][c-1]:
                    return c + grid[r][c]

                return -1
            
            elif grid[r][c] == 1 and c+1 < cols and grid[r][c] == grid[r][c+1]:
                return dfs(r+1, c+1)
            elif grid[r][c] == -1 and c-1 > -1 and grid[r][c] == grid[r][c-1]:
                return dfs(r+1, c-1)
            else:
                return -1
        
        ans = []
        for c in range(cols):
            ans.append(dfs(0, c))
        
        return ans
