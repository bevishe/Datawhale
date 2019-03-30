# _*_ coding:utf-8 _*_

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode):
        tree_list = []
        if root == None:
            return tree_list
        else:
            #
            tree_list.append([root,],)
            while(len(tree_list[0]) != 0):
                son_node_list = []
                temp = []
                for node in tree_list[0]:
                    if node != None:
                        if node.left != None:
                            temp.append(node.left)
                        if node.right != None:
                            temp.append(node.right)
                tree_list.insert(0,temp)
        return tree_list

if __name__ == '__main__':
   p = TreeNode(3)
   p.left = TreeNode(3)
   p.right = TreeNode(2)
   p.right.left = TreeNode(5)
   print(Solution().levelOrderBottom(p))