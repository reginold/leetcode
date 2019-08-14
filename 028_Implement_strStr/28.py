class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if not needle:
            return 0

        l = len(needle)
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if len(haystack) > i + l:
                    if haystack[i:i+l] == needle:
                        return i
        return -1

if __name__ == "__main__":
    solution = Solution()
    assert solution.strStr("hello", "ll") == 2
    assert solution.strStr("aaaaa", "bba") == -1
    print("Well Done, Go Summit")