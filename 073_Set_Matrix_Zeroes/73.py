class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix[0])
        n = len(matrix)
        FirstRow = False
        FirstCol = False
                   
        # 先判断第一行和第一列是否有0
        for i in range(m):
            if matrix[0][i] == 0:
                FirstRow = True
                break
        for i in range(n):
            if matrix[i][0] == 0:
                FirstCol = True
                break
        
        # 从第二行第二列开始寻找0，并将对应的第一行的位置放0
        for x in range(1,m):
            print(x)
            for y in range(1,n):
                if matrix[y][x] == 0:
                    matrix[y][0] = 0
                    matrix[0][x] = 0
                    
        # 看第一行中哪个元素等于0，将相对应的那一行都变成0  
        for i in range(1,m):
            if matrix[0][i] == 0:
                for j in range(n):
                    matrix[j][i] = 0
       
        # 看第一列中哪个元素等于0，将相对应的那一列都变成0  
        for i in range(n):
            if matrix[i][0] == 0:
                for j in range(m):
                    matrix[i][j] = 0
       
       
        if FirstRow:
            for i in range(m):
                matrix[0][i] = 0
        if FirstCol:
            for i in range(n):
                matrix[i][0] = 0