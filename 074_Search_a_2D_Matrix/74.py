class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 利用2个2分法
        # row和col各一次
        
        start = 0
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        row = -1
        
        while(start + 1 < m):
            mid = start + (m - start)/2
            if matrix[mid][n] < target:
                start = mid
            else:
                n = mid
        if matrix[start][n] >= target:
            row = start
        elif matrix[m][n] >= target:
            row = n
        else:
            return False
        
        start_col = 0
        end = n
        while (start_col+1 < end):
            mid = start_col + (end - start_col)/2
            if matrix[row][mid] < target:
                start_col = mid
            else:
                end = mid
        if (matrix[row][start_col] == target) and (matrix[row][end] == target):
            return True
        else:
            return False
        
        
        