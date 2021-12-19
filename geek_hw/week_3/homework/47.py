class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for i in nums:
            new_res = []
            for j in res:
                for n in range(len(j) + 1):
                    new_res.append(j[:n] + [i] + j[n:])
                    if n<len(j) and j[n]==i: break
            res = new_res
        return res