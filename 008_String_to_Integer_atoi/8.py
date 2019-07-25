import re


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        list = re.findall(r"[\+\-]*\d+", str)
        print(type(list[0]))
        if list == [] or (str[0].isdigit() == False and str[0] != "-" and str[0] != "+"):
            return 0
        elif ("+" and "-") in list[0]:
            return 0
        else:
            if int(list[0]) <= -2**31:
                return -2**31
            elif int(list[0]) >= 2**31-1:
                return 2**31-1
            else:
                pointer = 0
                for i in range(len(list[0])):
                    if list[0][i].isdigit():
                        pointer = i
                        break
                for pointer in range(len(list[0])):
                    if list[0][i].isdigit() == False:
                        return int(list[0][pointer:i])
                    else:
                        return int(list[0][pointer:])


if __name__ == "__main__":
    solution = Solution()
    print(solution.myAtoi("   -42"))
    assert solution.myAtoi("+-2") == 0
    assert solution.myAtoi("+1") == 1
    assert solution.myAtoi(".22") == 0
    assert solution.myAtoi("42") == 42
    assert solution.myAtoi("   -42") == -42
    assert solution.myAtoi("4193 with words") == 4193
    assert solution.myAtoi("words and 987") == 0
    assert solution.myAtoi("-91283472332") == -2147483648
    print("Well Done, Go Summit")
