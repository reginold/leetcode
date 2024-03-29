#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isSymmetric_check(root, root)

    def isSymmetric_check(self, left, right) -> bool:
        if left and right:
            return (
                left.val == right.val
                and self.isSymmetric_check(left.left, right.right)
                and self.isSymmetric_check(left.right, right.left)
            )
        else:
            return left == right


# @lc code=end