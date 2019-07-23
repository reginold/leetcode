class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        pointer = 0
        maxlen = 0
        for index, value in enumerate(s):
            if value in dict:
                pointer = max(dict[value] + 1, pointer)
            maxlen = max(index-pointer+1, maxlen)
            dict[value] = index   
        return maxlen

if __name__ == "__main__":
    solution = Solution()
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
    print("Well Done, Go Summit")