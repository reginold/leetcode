class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        # 查找list的元素
        
        for element in matrix:
            print(element)
            if target in element:
                return True
        return False