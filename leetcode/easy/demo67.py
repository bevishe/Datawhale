class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)
        re = []
        ex_count = 0
        if len_a < len_b:
            for i in range(0,len_b):
                if i >= len_a:
                    re.append(str((ex_count + int(b[-1-i]))%2))
                    ex_count = 0 if ex_count + int(b[-1-i]) <= 1 else 1
                else:
                    re.append(str((int(a[-1-i]) + int(b[-1-i]) + ex_count)%2))
                    ex_count = 0 if int(a[-1-i]) + int(b[-1-i]) + ex_count == 0 or int(a[-1-i]) + int(b[-1-i]) + ex_count == 1 else int(a[-1-i]) + int(b[-1-i]) + ex_count == 2 or int(a[-1-i]) + int(b[-1-i]) + ex_count == 3
        elif len_a > len_b:
            for i in range(0, len_a):
                if i >= len_b:
                    re.append(str((ex_count + int(a[-1-i])) % 2))
                    ex_count = 0 if ex_count + int(a[-1-i]) <= 1 else 1
                else:
                    re.append(str((int(a[-1-i]) + int(b[-1-i]) + ex_count)%2))
                    ex_count = 0 if int(a[-1-i]) + int(b[-1-i]) + ex_count == 0 or int(a[-1-i]) + int(b[-1-i]) + ex_count == 1 else int(a[-1-i]) + int(b[-1-i]) + ex_count == 2 or int(a[-1-i]) + int(b[-1-i]) + ex_count == 3
        else:
            for i in range(0,len_a):
                re.append(str((int(a[-1-i]) + int(b[-1-i]) + ex_count) % 2))
                ex_count = 0 if int(a[-1-i]) + int(b[-1-i]) + ex_count == 0 or int(a[-1-i]) + int(b[-1-i]) + ex_count == 1 else int(
                    a[-1-i]) + int(b[-1-i]) + ex_count == 2 or int(a[-1-i]) + int(b[-1-i]) + ex_count == 3

        if ex_count != 0:
            re.append('1')
        re.reverse()
        string = ''.join(re)
        return string

if __name__ == '__main__':
    print(Solution().addBinary('1010','1011'))