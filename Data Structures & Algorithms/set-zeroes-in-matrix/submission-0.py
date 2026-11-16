class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        cols = set()
        for i in range(n):
            has_zero = False
            for j in range(m):
                if matrix[i][j] == 0:
                    has_zero = True
                    cols.add(j)
            if has_zero:
                matrix[i] = [0] * m
        for x in cols:
            for y in range(n):
                matrix[y][x] = 0


                
                

        
        