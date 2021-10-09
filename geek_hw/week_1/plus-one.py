from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break

            if digits[0] == 0:
                res = [0] + digits
                res[0] = 1
                return res
        return digits
