class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        # 先将list升位排序
        nums = sorted(nums)
        for i in range(len(nums)-2):
            # 如果有一个数是大于0的，那么三个整数相加一定是大于0的 直接break
            if nums[i] > 0:
                break
            # 如果i的数和i+1是相等的情况下，直接进行下一个数，一样的数得到的总和是没有变化的
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # 这里的算法想法可以参考11题，基本上一模一样
            l = i+1
            r = len(nums) - 1
            while l < r:
                sum_all = nums[i] + nums[l] + nums[r]
                if sum_all < 0:
                    l += 1
                elif sum_all > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # 同上面，一样的数字直接跳过
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res


if __name__ == "__main__":
    solution = Solution()
    assert solution.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1,-1,2],[-1,0,1]]
    print("Well Done, Go Summit")
