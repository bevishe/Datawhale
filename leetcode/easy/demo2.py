# _*_ coding:utf-8 _*_

class Solution:
    def maxSubArray(self, nums) -> int:
        max_count = nums[0] if len(nums) != 0 else None
        sum = 0
        for num in nums:
            if sum > 0:
                sum += num
            else:
                sum = num
            max_count = max(sum,max_count)
        return max_count

if __name__ == '__main__':
    print(Solution().maxSubArray([1,2,3,-6,-6,2,3,-9]))

