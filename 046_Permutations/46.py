class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = [[]]
        for n in nums:
            new_res = []
            for perm in res:
                for i in range(len(perm)+1):
                    new_res.append(perm[:i] + [n] + perm[i:])
            res = new_res
        return res


if __name__ == "__main__":
    solution = Solution()
    assert solution.permute([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [
        2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    print("Well Done, Go Summit")
