# _*_ coding:utf-8 _*_

"""
author:Bevishe
date:2019-05-02
"""

'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。
'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # 将两个list变为一个list然后求新的list的中卫数
        if nums1.__len__() == 0:
            return nums2[nums2.__len__()//2] if nums2.__len__() % 2 ==1 else (nums2[nums2.__len__()//2 - 1]+nums2[nums2.__len__()//2])/2
        elif nums2.__len__() == 0:
            return nums1[nums1.__len__()//2] if nums1.__len__() % 2 ==1 else (nums1[nums1.__len__()//2 - 1]+nums1[nums1.__len__()//2])/2
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        return nums1[nums1.__len__()//2] if nums1.__len__() % 2 ==1 else (nums1[nums1.__len__()//2 - 1]+nums1[nums1.__len__()//2])/2



if __name__ == '__main__':
    nums1 = [1,3,4]
    nums2 = [2]
    print(Solution().findMedianSortedArrays(nums1,nums2))
