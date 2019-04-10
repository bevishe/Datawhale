class Solution:
    def getRow(self,rowIndex):
        res = [[1], ]
        if rowIndex == 1: return res
        up_floor = [1]
        for i in range(1, rowIndex):
            down_floor = []
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    down_floor.insert(j, 1)
                else:
                    if j - 1 >= 0 and j <= i - 1:
                        down_floor.insert(j, up_floor[j - 1] + up_floor[j])
            res.append(down_floor)
            up_floor = down_floor
        return res[rowIndex-1]

if __name__ == '__main__':
    print(Solution().getRow(3))