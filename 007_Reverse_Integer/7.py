class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 2**31-1 or x <= -2**31:
            return 0
        else:
            rev = 0
            x_abs = abs(x)
            while x_abs != 0:
                num = x_abs % 10
                x_abs= x_abs // 10
                rev = rev*10 + num
            if rev >= 2**31-1 or rev <= -2**31:
                return 0
            elif x >= 0:
                return rev
            elif x < 0:
                return -rev

if __name__ == "__main__":
    solution = Solution()
    assert solution.reverse(0) == 0
    assert solution.reverse(1534236469) == 0
    assert solution.reverse(123) == 321
    assert solution.reverse(-123) == -321
    assert solution.reverse(120) == 21
    print("Well Done, Go Summit")
