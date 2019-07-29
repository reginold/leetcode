class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        for i in range(0,len(height)-1):
            for j in range(i+1, len(height)):
                #取小的值*区间相减
                res = max(res, min(height[i],height[j])*(j-i))
        return res



if __name__ == "__main__":
    solution = Solution()
    assert solution.maxArea([1,8,6,2,5,4,8,3,7]) == 49
    print("Well Done, Go Summit")