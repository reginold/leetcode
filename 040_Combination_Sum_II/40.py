class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 和39题一样，还是利用DFS的方法遍历每一个list
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, res, [])
        return res
    
    def dfs(self, nums, target, index, res, path):
    # 如果数字之和等于target，我们将这写数字添加到list
        if not target:
            return res.append(path)
        for i in range(index, len(nums)):
            # 重合的数字跳过
            if i > index and nums[i] == nums[i - 1]:
                continue 
            elif target < nums[i]:
                break
            self.dfs(nums, target - nums[i], i+1, res, path + [nums[i]])