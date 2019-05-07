# _*_ coding:utf-8 _*_
"""
author:Bevishe
date:2019-05-07
"""

'''
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
'''
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.minStack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.minStack[-1] if len(self.minStack) != 0 else None

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.minStack)