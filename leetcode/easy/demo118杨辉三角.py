# _*_ coding:utf-8 _*_

# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# 在杨辉三角中，每个数是它左上方和右上方的数的和。

class Solution:
    def generate(self, numRows: int):
        res = [[1],]
        if numRows == 1: return res
        up_floor = [1]
        for i in range(1,numRows):
            down_floor = []
            for j in range(0,i + 1):
                if j == 0 or j == i:
                    down_floor.insert(j,1)
                else:
                    if j - 1 >= 0 and j<= i - 1:
                        down_floor.insert(j,up_floor[j-1] + up_floor[j])
            res.append(down_floor)
            up_floor = down_floor
        return res

if __name__ == '__main__':
    print(Solution().generate(4))
