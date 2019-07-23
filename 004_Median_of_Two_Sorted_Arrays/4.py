class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        list_new = sorted(nums1 + nums2)
        leng = len(list_new)
        if leng%2 == 0:
            return float((list_new[int(leng/2)-1] + list_new[int(leng/2)])/2)
        else:
            return float(list_new[len(list_new)/2])
    

if __name__ == "__main__":
    solution = Solution()
    assert solution.findMedianSortedArrays([1,2],[3,4]) == 2.5
    print("Well Done, Go Summit")