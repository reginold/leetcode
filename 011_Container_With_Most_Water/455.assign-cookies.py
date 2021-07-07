#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: list, s: list) -> int:
        g = sorted(g, reverse=True)
        s = sorted(s, reverse=True)
        i = 0
        j = 0
        ans = 0
        while (i < len(g)) and (j < len(s)):
            if g[i] <= s[j]:
                i += 1
                j += 1
                ans += 1
            else:
                i += 1
        return ans


# @lc code=end
