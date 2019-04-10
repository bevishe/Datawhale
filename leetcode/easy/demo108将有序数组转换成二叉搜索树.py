# _*_ coding:utf-8 _*_
# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
#
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
# 示例:
#
# 给定有序数组: [-10,-3,0,5,9],
#
# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        # 将数组变换成高度平衡二叉搜索树的数组形式


        root = TreeNode(nums[0]) if len(nums) != 0 else None
        if len(nums) != 0:
            p = root
            temp = [root,]
            i = 1
            while(i != len(nums) - 1):
                for node in temp:
                    node.left = TreeNode(nums[i]) if nums[i] != 'null' else None
                    node.right = TreeNode(nums[i]) if nums[i] != 'null' else None
                temp_next_node = []
                if node.left != None:
                    temp_next_node.append(node.left)
                if node.right != None:
                    temp_next_node.append(node.right)
                temp = temp_next_node
            return root
        return root

if __name__ == '__main__':
    root = Solution().sortedArrayToBST([0,-3,9,-10,'null',5])
    print(root.val)
    print(root.left.val)
    print(root.right.val)