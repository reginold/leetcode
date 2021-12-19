class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp)<=n:
            dp += [min(dp[-c*c] for c in range(1, int(len(dp)**0.5+1))) + 1]
            # print(dp)
        return dp[n]