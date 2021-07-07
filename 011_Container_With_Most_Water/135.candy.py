#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        init = [1] * len(ratings)
        for i in range(len(ratings) - 1):
            if ratings[i] < ratings[i + 1]:
                init[i + 1] = init[i] + 1
        for i in range(len(ratings) - 1):
            index = len(ratings) - 1 - i
            if ratings[index - 1] > ratings[index] and init[index - 1] <= init[index]:
                init[index - 1] = init[index] + 1
        return sum(init)


# @lc code=end
