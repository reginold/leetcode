class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        比如我们把board[i][j]
        """
        # 用字符串:

        # 表示行:(i) + board[i][j]

        # 表示列: board[i][j] + (j)

        # 表示小正方形:(i) + board[i][j] + (j)

        # 就直接可以用一个集合搞定!
        
        
        one_set = set()
     
        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    row = "(" + str(i) + ")" + board[i][j]
                    col = board[i][j] + "(" + str(j) + ")"
                    small_square = "(" + str(i//3)+ ")" + board[i][j] +  "(" + str(j//3) + ")"
                    if row in one_set or col in one_set or small_square in one_set:
                        return False
                    one_set.update([row,col,small_square])
                    
        return True

if __name__ == "__main__":
    solution = Solution()
    assert solution.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]) == True
    assert solution.isValidSudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]) == False
    print("Well Done, Go Summit")
