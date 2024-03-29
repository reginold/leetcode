/*
 * @lc app=leetcode id=101 lang=javascript
 *
 * [101] Symmetric Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function (root) {
	if (root == null) return true;
	return dfs(root.left, root.right);
};

function dfs(left, right) {
	if (left == null && right == null) return true;
	if (left == null || right == null) return false;
	if (left.val != right.val) return false;
	return dfs(left.left, right.right) && dfs(left.right, right.left)
}
// @lc code=end

