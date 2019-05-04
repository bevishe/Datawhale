# _*_ coding:utf-8 _*_
"""
author:Bevishe
date:2019-05-02
"""


'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
'''

class Solution:
	def convert(self,s,numRows):
		columns = (s.__len__()//(2*numRows - 1))
		if (s.__len__() % (2*numRows - 1)>numRows):
			columns += (s.__len__() % (2*numRows - 1)-numRows)
		a = []
		for i in range(numRows):
			a.append([])
			for j in range(columns):
				a[i].append(0)
		a[1][1] = 'A'
		return a
if __name__ == '__main__':
	print(Solution().convert("sfdasdfasdf",3))