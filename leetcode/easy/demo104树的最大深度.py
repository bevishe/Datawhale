# _*_ coding:utf-8 _*_
# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最大深度 3 。
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 用来递归，没有下一层就返回False
    def hasDeep(self,leftNode,rightNode):
        pass
    def maxDepth(self, root: TreeNode) -> int:
        que = [root]
        deep_count = 0
        while(len(que) != 0):
            que_son_node = []
            deep_count += 1
            for node in que:
                if node != None:
                    if node.left != None:
                        que_son_node.append(node.left)
                    if node.right != None:
                        que_son_node.append(node.right)
            que = que_son_node
        return deep_count

if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    p.left.left = TreeNode(4)
    print(Solution().maxDepth(p))