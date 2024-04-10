class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i>0 and j>0 and matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True
