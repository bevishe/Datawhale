# _*_ coding:utf-8 _*_
"""
author:Bevishe
date:2019-05-07
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 快慢指针判断是否是个环链表
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        x1 = head
        x2 =head
        while(x1 and x2 and x2.next and x2.next.next):
            x1 = x1.next
            x2 = x2.next.next
            if x1 == x2:
                return True
        return False

