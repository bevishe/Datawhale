# _*_ coding:utf-8 _*_
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self) -> str:
        string = ''
        while(self.next != None):
            string = string + str(self.val) + '->'
            self = self.next

        return string + str(self.val)


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p_node = head
        while(p_node.next != None):
            if p_node.val == p_node.next.val:
                p_node.next = p_node.next.next
            p_node = p_node.next
        return head


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    print(l1)
    print(Solution().deleteDuplicates(l1))