# _*_ coding:utf-8 _*_
"""
author:Bevishe
date:2019-05-04
"""

'''
找到第一个非空的字符（数字，-，+，其他，后面是数组累加，其他return）

'''




class Solution:
	def myAtoi(self, str: str):
		firstFlag = True
		numFlag = True
		new_str = []
		nums = ['1','2','3','4','5','6','7','8','9','0']
		for s in str:
			if firstFlag:
				if s == " ":
					pass
				elif s == '-' or s == '+':
					new_str.append(s)
					firstFlag = False
				elif s in nums:
					new_str.append(s)
					firstFlag = False
					numFlag = False
				else:
					return 0
			elif numFlag:
				if s not in nums or s == ' ':
					return 0
				elif s in nums:
					new_str.append(s)
					numFlag = False
				else:
					return 0
			else:
				if s in nums:
					new_str.append(s)
				else:
					break
		if len(new_str) == 0 or (len(new_str) == 1 and (new_str[0] == '-'or new_str[0] == '+')):
			return 0
		else:
			if new_str[0] == '-' or new_str[0] == '+':
				num = -int("".join(new_str[1:])) if new_str[0] == '-' else int("".join(new_str[1:]))
			else:
				num = int("".join(new_str))
		if num < -2**31:
			return 2**31
		elif num > 2**31 - 1:
			return 2**31 -1
		else:
			return num


if __name__ == '__main__':
	print(Solution().myAtoi("3.14159"))

