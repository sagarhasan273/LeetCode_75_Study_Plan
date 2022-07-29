class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, 0
        res = []
        while r < rows and c < cols:

            for j in range(c, cols):
                res.append(matrix[r][j])
            r += 1
            
            for i in range(r, rows):
                res.append(matrix[i][cols-1])
            cols -= 1
            
            if r < rows:
                for j in range(cols-1, c-1, -1):
                    res.append(matrix[rows-1][j])
                rows -= 1
            
            if c < cols:
                for i in range(rows-1, r-1, -1):
                    res.append(matrix[i][c])
                c += 1
            
        return res