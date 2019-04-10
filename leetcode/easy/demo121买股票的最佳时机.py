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
        # 1.求取所有升序子数组的其实index
        min_index_list = []
        for i in range(0,len(prices)):
            if i == 0:
                min_index_list.append(0)
            elif i + 1 <= len(prices) - 1 and prices[i] > prices[i]:
                min_index_list.append(i+1)
        # 2.将所有子数组中的最后一个数加到max_num_list中，返回最大值，和




        return maxPrice

if __name__ == '__main__':
    print(Solution().maxProfit([1,2,3,4,5,10,1]))