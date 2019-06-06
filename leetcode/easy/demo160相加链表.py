# _*_ coding:utf-8 _*_
"""
author:Bevishe
date:2019-05-08
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 首先遍历出来a b的长度
        pA = headA
        pB = headB
        count  = 0
        while pA != None:
            pA = pA.next
            count += 1
        while pB != None:
            pB = pB.next
            count -= 1

        # 先判断是否相交即最后一个元素的地址是否相等
        if pA == pB:
            pA = headA
            pB = headB
            if count >= 0:
                for i in range(count):
                    pA = pA.next
            else:
                for i in range(-count):
                    pB = pB.next
            while(pA != pB):
                pA = pA.next
                pB = pB.next
            return pA.val
        else:
            return None

if __name__ == '__main__':
    l = ListNode(3)
    l.next = ListNode(4)
    l.next = ListNode(5)
    headA = ListNode(1)
    headA.next = l
    headB = ListNode(6)
    headB.next = ListNode(7)
    headB.next.next = ListNode(8)
    headB.next.next = l
    print(Solution().getIntersectionNode(headA,headB))