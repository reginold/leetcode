class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thousands =["", "M", "MM", "MMM"]
        print(1994 // 1000 % 10)
        return thousands[num // 1000 % 10] + hundreds[num // 100 % 10] + tens[num // 10 % 10] + ones[num % 10]


if __name__ == "__main__":
    solution = Solution()
    assert solution.intToRoman(1994) == "MCMXCIV"
    print("Well Done, Go Summit")


