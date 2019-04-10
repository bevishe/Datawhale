class Solution:
    def letterCombinations(self, digits: str):
        dic = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],
               '5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],
               '8':['t','u','v'],'9':['w','x','y','z']
        }

        def generator_list(list1,list2):
            re_list = []
            for _ in list1:
                for __ in list2:
                    re_list.append(str(_)+str(__))
            return re_list

        if digits.__len__() == 2:
            return generator_list(dic.get(digits[0]),dic.get(digits[1]))
        elif digits.__len__() == 0:
            return []
        elif digits.__len__() == 1:
            return dic.get(digits[0])
        else:
            re_list = generator_list(dic.get(digits[0]),dic.get(digits[1]))
            for i in range(2,digits.__len__()):
                re_list = generator_list(re_list,dic.get(digits[i]))
            return re_list

if __name__ == '__main__':
    print(Solution().letterCombinations('2332'))