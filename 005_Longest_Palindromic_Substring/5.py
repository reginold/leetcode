class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start, end = 0, 0
        if len(s) < 1 or not s:
            return ""
        for i in range(len(s)):
            len1 = self.interval_cal(s, i, i)
            len2 = self.interval_cal(s, i, i+1)
            maxlen = max(len1, len2)
            if (maxlen > end - start):
                start = i - (maxlen - 1)//2
                end = i + maxlen//2
                
        return s[start: end+1]

    def interval_cal(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return r-l-1


if __name__ == "__main__":
    solution = Solution()
    assert solution.longestPalindrome("babad") == "aba"
    assert solution.longestPalindrome("cbbd") == "bb"
    print("Well Done, Go Summit")
