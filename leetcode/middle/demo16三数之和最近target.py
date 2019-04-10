class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        sum_count = sum(nums[0]+nums[1]+nums[-1])
        min_with_target = abs(sum_count - target)
        if min_with_target == 0:
            reutrn sum_count
        for i in range(0,len(nums)-2):
            k = len(nums) - 2
            for j in range(i+1,k):
                if j+1 < k and nums[i] + nums[j] +
        pass