class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        l = 0
        r = len(height)-1
        res = 0
        while l < r:
            res = max(res, min(height[l], height[r])*(r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return(res)


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    print("Well Done, Go Summit")
