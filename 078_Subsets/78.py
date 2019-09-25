class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.helper(nums,0,res,[])
        return res
    
    def helper(self, nums, index, res, curr):
        res.append(curr)
        for i in range(index,len(nums)):
            print("i="+ str(i))
            print("=====")
            self.helper(nums, i+1, res, curr+[nums[i]])
            print(curr)
        return res