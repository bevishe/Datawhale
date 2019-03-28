# _*_ coding:utf-8 _*_
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p:TreeNode, q:TreeNode)-> bool:
        if not p and not q:
            return True
        elif p is not None and q is not None:
            if p.val == q.val:
                return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
            else:
                return False
        else:
            return False


if __name__ == '__main__':
    p = TreeNode(1)
    q = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(4)
    q.left = TreeNode(2)
    q.right = TreeNode(2)
    print(Solution().isSameTree(p,q))