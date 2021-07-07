from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ops = {
            "-": lambda x, y: x - y,
            "+": lambda x, y: x + y,
            "*": lambda x, y: x * y,
        }

        def cal(expression):
            res = []
            for i in range(len(expression)):
                if expression[i] == "+" or expression[i] == "*" or expression[i] == "-":
                    left_list = expression[:i]
                    res1 = evaluate(left_list)
                    # res.append(res1)
                    right_list = expression[i + 1 :]
                    res2 = evaluate(right_list)
                    # res.append(res2)
                    res.append(ops[expression[i]](int(res1), int(res2)))
                else:
                    continue
            return res

        def evaluate(express):
            if len(express) > 3:
                cal(express)
            return eval(express)

        my_results = []
        if len(expression) <= 3:
            my_results.append(eval(expression))
            return my_results
        else:
            l = cal(expression)
            return l


if __name__ == "__main__":
    solution = Solution()
    s = "2*3-4*5"
    result = solution.diffWaysToCompute(s)
    print(result)

# 2部分， 一个是数字 一个是符号 两个list
# 出现的形式 一定是 数字 符号 数字 符号
# 括号的排列组合 这是个难点 如何进行
# 分两个 一个括号
#
#
#
#
#
#
