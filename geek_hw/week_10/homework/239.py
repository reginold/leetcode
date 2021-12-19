class AVLTreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
        self.cnt = 1
class AVLTree(object):
    def getHeight(self, root):
        return 0 if root is None else root.height

    def getBalance(self, root):
        return 0 if root is None else self.getHeight(root.left) - self.getHeight(root.right)

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1+max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1+max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1+max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1+max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def insert(self, root, key):
        if not root:
            return AVLTreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        elif key > root.val:
            root.right = self.insert(root.right, key)
        else:
            root.cnt += 1
            return root

        # step2- update the height of the ancesotr node

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        balance = self.getBalance(root)

        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root

    def delete(self, root, key):
        if not root:
            return root
        elif key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            if root.cnt > 1:
                root.cnt -= 1
                return root
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)

        if root is None:
            return root
        root.height = 1+max(self.getHeight(root.left),
                            self.getHeight(root.right))
        balance = self.getBalance(root)

        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)

        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)

        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def getMaxValueNode(self, root):
        if root is None or root.right is None:
            return root
        return self.getMaxValueNode(root.right)
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n, ans = len(nums),[]
        if n==0 or k==1:
            return nums
        avl = AVLTree()
        root = None
        for x in range(k):
            root = avl.insert(root,nums[x])
        ans.append(avl.getMaxValueNode(root).val)
        for x in range(k,n):
            root=avl.delete(root,nums[x-k])
            root=avl.insert(root,nums[x])
            ans.append(avl.getMaxValueNode(root).val)
        return ans