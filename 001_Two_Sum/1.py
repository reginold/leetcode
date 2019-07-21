class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        
        for i, num in enumerate(nums):
            if (target - num) in dict:
                return(dict[target - num], i)
            else:
                dict[num] = i


if __name__ == '__main__':
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) == (0, 1)
    print("Well Done.Go Summit")
