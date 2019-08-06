# rutime: 84ms, faster than 25.89%
# memory usage: 13.5MB, less than 92.61%

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 当空list，返回0
        if len(nums) == 0:
            return 0
        # 一个 pointer遍历list，发现相同的就删除一个元素
        pointer = 0
        while pointer < len(nums)-1:
            if nums[pointer] == nums[pointer+1]:
                del nums[pointer]
            else:
                pointer += 1
        return len(nums)


if __name__ == "__main__":
    solution = Solution()
    solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5
    print("Well Done, Go Summit")