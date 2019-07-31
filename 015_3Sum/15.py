class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        resultList = []
        nums.sort()
        for i in range(0,length-2):
            j = i + 1
            k = length - 1
            while (j < k):
                sum0 = nums[i] + nums[j] + nums[k]
                if (sum0 == 0):
                    result = []
                    result.append(nums[i])
                    result.append(nums[j])
                    result.append(nums[k])
                    if result not in resultList:
                        resultList.append(result)
                    j +=1
                if (sum0 < 0):
                    j +=1
                if (sum0 > 0):
                    k -=1
        return resultList        
       


if __name__ == "__main__":
    solution = Solution()
    assert solution.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1],[-1, -1, 2]]
    print("Well Done, Go Summit")