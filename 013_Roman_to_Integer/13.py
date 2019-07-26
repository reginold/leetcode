class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        dict = {"I": 1, "V": 5, "X": 10, "L": 50,
                "C": 100, "D": 500, "M": 1000}
        for i in range(0, len(s) - 1):
            if dict[s[i]] < dict[s[i+1]]:
                result -= dict[s[i]]
            else:
                result += dict[s[i]]
        return result + dict[s[-1]]


if __name__ == "__main__":
    solution = Solution()
    assert solution.romanToInt("LVIII") == 58
    print("Well Done, Go Summit")
