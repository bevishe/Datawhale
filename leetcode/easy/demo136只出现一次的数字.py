# _*_ coding:utf-8 _*_
"""
author:Bevishe
date:2019-05-07
"""

'''
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
'''

class Solution:
	def singleNumber(self,nums):
		nums.sort()
		for i in range(nums.__len__() - 1):
			if i == 0 and nums[i] == nums[i+1]:
				pass
			elif nums[i-1] == nums[i] or nums[i] == nums[i+1]:
				pass
			else:
				return nums[i]
		return nums[-1]

	def singleNumber2(self,nums):
		a = 0
		for num in nums:
			a = a ^ num
		return a

if __name__ == '__main__':
	print(Solution().singleNumber([2,2,1,1,4,1,3,2,3,1]))