class Solution:
    def rotate_matrix_by_90(self,matrix,n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] ,matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(n):
            matrix[i] = matrix[i][::-1]
        return matrix

so = Solution()
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
n = 4
newMatrix = so.rotate_matrix_by_90(matrix,n)
print(newMatrix)



