class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        if rows == 0:
            return 0
        
        dp = [0 for x in range(rows)]
        dp[0] = triangle[0][0]
        for row in range(1, rows):
            dp[row] = triangle[row][row] + dp[row-1]
            for col in range(row-1, 0, -1):
                dp[col] = triangle[row][col] + min(dp[col], dp[col-1])
            dp[0] += triangle[row][0]
        
        res = dp[0]
        for x in dp:
            if x < res:
                res = x
        return res