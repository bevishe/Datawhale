class Solution:
    def climbStairs(self, n: int) -> int:
        two_step_count = n // 2
        count = 1
        for i in range(1,two_step_count + 1):
            the_all_count = i + (n - 2 * i)
            # 计算C n i
            count_son = 1
            count_mother = 1
            for j in range(0,i):
                count_son *= (the_all_count - j)
            for j in range(1,i+1):
                count_mother *= j
            count += count_son // count_mother
        return count

if __name__ == '__main__':
    print(Solution().climbStairs(34))