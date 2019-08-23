class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(candidates, target, 0, res, [])
        return res

    def dfs(self, nums, target, index, res, path):
        if target < 0:
            return
        elif target == 0:
            return res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, target - nums[i], i, res, path + [nums[i]])


if __name__ == "__main__":
    solution = Solution()
    assert solution.combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert solution.combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2],[2, 3, 3],[3, 5]]
    print("Well Done, Go Summit")
