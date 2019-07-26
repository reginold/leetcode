class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        for i, ch in enumerate(zip(*strs)):
            if (len(set(ch))) > 1:
                return strs[0][:i]
        else:
            return min(strs)

if __name__ == "__main__":
    solution = Solution()
    assert solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    print("Well Done, Go Summit")
