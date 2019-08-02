class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # 设置比较的初始值，最小的三个和
        res = sum(nums[:3])
        # 先将list升位排序
        nums = sorted(nums)
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums) - 1
            while l < r:
                sum_all = nums[i] + nums[l] + nums[r]
                # 重点：如果总和-tar 绝对值 是小于 初始总和-tar的 绝对值的话 就取现在的值 
                if abs(sum_all - target) < abs(res - target):
                    res = sum_all
                if sum_all < target:
                    l += 1
                elif sum_all > target:
                    r -= 1
                # 如果这里不返回，将会出现time limit exceeded，不会跳出循环
                else:
                    return res
        return res 
                
         


if __name__ == "__main__":
    solution = Solution()
    assert solution.threeSumClosest([-1, 2, 1, -4], 1) == 2
    print("Well Done, Go Summit")