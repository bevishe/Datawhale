# _*_ coding:utf-8 _*_
# 给定一个二叉树，检查它是否是镜像对称的。
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
# 说明:
#
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric_(self,r, t):
        if r == None and t == None:
            return True
        if r == None or t == None:
            return False
        if r.val != t.val:
            return False
        return self.isSymmetric_(r.left,t.right) and self.isSymmetric_(r.right,t.left)


    def isSymmetric(self, root: TreeNode) -> bool:
      # 使用递归的思想来
        if root == None:
            return True
        return self.isSymmetric_(root.left,root.right)


if __name__ == '__main__':
    p = TreeNode(2)
    p.left = TreeNode(3)
    p.right = TreeNode(3)
    print(Solution().isSymmetric(p))
