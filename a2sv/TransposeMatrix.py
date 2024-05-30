class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        # res = [[0]*len(matrix) for _ in range(len(matrix[0]))]
        # for r in range(len(matrix)):
        #     for c in range(len(matrix[0])):
        #         res[c][r] = matrix[r][c]
        # return res
        res = []
        for c in range(len(matrix[0])):
            temp = []
            for r in range(len(matrix)):
                temp.append(matrix[r][c])
            res.append(temp)
        return res
