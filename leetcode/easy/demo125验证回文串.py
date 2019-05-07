# _*_ coding:utf-8 _*_
"""
author:Bevishe
date:2019-05-07
"""
'''
只考虑一个字符串中的字母和数字字符
'''

class Solution:
	def isPalindrome(self,s:str):
		new_str = ""
		for _ in s:
			if _.isalnum() or _.isalpha():
				new_str += _.upper()
		for i in range(new_str.__len__()//2):
			if new_str[i] != new_str[new_str.__len__() - i - 1]:
				return False
		return True


if __name__ == '__main__':
	print(Solution().isPalindrome("race a car"))