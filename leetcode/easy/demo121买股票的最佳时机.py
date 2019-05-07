# _*_ coding:utf-8 _*_

class Solution():
    def maxProfit(self,prices):
        '''
        思路：遍历prices数组，记录其中每个从小到大的子数组的第一个元素在prices中的
        下标，然后找每个子数组最后一个元素组成的数组中最大的数，然后找这个小标之前的所有
        子数组的第一个元素组合起来的元素值最小的一个，相减得出最大利润
        :param prices:
        :return:
        '''
        max = 0
        for i in range(prices.__len__()):
            for j in range(i+1,prices.__len__()):
                if max < prices[j] - prices[i]:
                    max = prices[j] - prices[i]
        return max
if __name__ == '__main__':
    print(Solution().maxProfit([1,2,3,4,5,10,1]))