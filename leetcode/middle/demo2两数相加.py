# _*_ coding:utf-8 _*_
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		'''
		直接将链表中的数变为10进制，相加，让后变为列表形式
		:param l1:
		:param l2:
		:return:
		'''
		def list_to_int(l1):
			num = 0
			count = 0
			while(l1 != None):
				num = num + l1.val*(10**(count))
				count += 1
				l1 = l1.next
			return num

		twoSum = list_to_int(l1) + list_to_int(l2)
		num_list = list(str(twoSum))
		num_list.reverse()
		print(num_list)
		re = ListNode(int(num_list[0]))
		head = re
		for i in range(1,num_list.__len__()):
			re.next = ListNode(num_list[i])
			re = re.next
		print()
		return head

if __name__ == '__main__':
	l1 = ListNode(1)
	l1.next = ListNode(2)
	l1.next.next = ListNode(3)

	l2 = ListNode(3)
	l2.next = ListNode(2)
	print(Solution().addTwoNumbers(l1,l2))