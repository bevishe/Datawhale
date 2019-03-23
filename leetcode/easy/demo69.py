class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        else:
            count = 1
            x_ = x
            while(x_ > 4):
                count *= 2
                x_ //= 4
            count = count - 1
            while(count*count <= x):
                count += 1
            return count - 1
if __name__ == '__main__':
    print(Solution().mySqrt(8))