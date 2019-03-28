# _*_ coding:utf-8 _*_

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self) -> str:
        string = ''
        while(self.next != None):
            string = string + str(self.val) + '->'
            self = self.next
        return string + str(self.val)

    def addNode(self,val):
        while(self.next != None):
            self = self.next
        self.next = ListNode(val)

class TreeNode(object):
    def __init__(self, x):
        self.parent = None          # root.parent = None
        self.val = x
        self.left = None
        self.right = None


    def addLeftNode(self,val):
        self.left = TreeNode(val)
        self.parent = self

    def addRightNode(self,val):
        self.right = TreeNode(val)
        self.parent = self

    # 对树进行先序遍历
    def preorder_traversal(self,tree_list):
        if self.val  != None:
            tree_list.append(self.val)
        if self.left != None:
            self.left.preorder_traversal()
        if self.right != None:
            self.right.preorder_traversal()


    # 对树进行中序遍历
    def sequential_traversal(self):
        pass

    # 对树进行后序遍历
    def post_order_traversal(self):
        pass




# 平衡二叉树
class BalancedBinaryTree(object):
    pass

if __name__ == '__main__':
    treeNode = TreeNode(1)
    treeNode.addLeftNode(-1)
    treeNode.addRightNode(2)
    tree_list = []
    treeNode.preorder_traversal(tree_list)
    print(tree_list)