class Solution(object):
    def searchMatrix(self, matrix, target):
        # number of rows and columns
        rows = len(matrix)
        cols = len(matrix[0])

        # pointers
        left = 0
        right = rows * cols - 1

        while left <= right:
            middle = left + (right - left) // 2
            # find the middle row and col
            row = middle // cols
            col = middle % cols

            if target > matrix[row][col]:
                left = middle + 1
            elif target < matrix[row][col]:
                right = middle - 1
            else:
                return True
        
        return False