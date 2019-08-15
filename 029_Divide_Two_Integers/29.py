class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = -1 if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        if dividend < divisor:
            return 0
        elif dividend == divisor:
            return flag
        # 判断是否在区间内
        elif divisor == 1:
            return flag*dividend if flag*dividend < 2**31 else 2**31-1
        else:
            print(flag*len(range(divisor, dividend+1, divisor)))
            return flag*len(range(divisor, dividend+1, divisor))

if __name__ == "__main__":
    solution = Solution()
    assert solution.divide(-2147483648,2) == -1073741824
    assert solution.divide(10, 3) == 3
    assert solution.divide(7, -3) == -2
    print("Well Done, Go Summit")