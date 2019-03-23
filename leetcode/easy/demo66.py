class Solution:
    def plusOne(self, digits):
        sum_count = 0
        for i in range(1,len(digits) + 1):
            sum_count = sum_count + digits[0 - i]*(10**(i-1))
        sum_count += 1
        re_list = []
        for _ in str(sum_count):
            re_list.append(int(_))
        return re_list

if __name__ == '__main__':
    print(Solution().plusOne([1,2,3]))