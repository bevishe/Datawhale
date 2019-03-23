class Solution:
    def countAndSay(self, n: int) -> str:
        string = ''
        for i in range(1, n + 1):
            # 每层返回一个字符串
            if i == 1:
                string += '1'
            else:
                len_string = len(string)
                new_string = ''
                for j in range(0, len_string):
                    if j + 1 <= len_string - 1 and string[j] == string[j + 1]:
                        new_string = new_string + '2' + string[j]
                        j = j + 2
                        if j  > len_string - 1:
                            break
                    elif j + 1 <= len_string - 1 and string[j] != string[j + 1]:
                        new_string = new_string + '1' + string[j]
                        j += 1
                    elif j == len_string:
                        string = new_string
                    else:
                        new_string = new_string + '1' + string[j]
                        string = new_string
        return string

if __name__ == '__main__':
    print(Solution().countAndSay(3))