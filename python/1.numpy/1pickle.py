# _*_ coding:utf-8 _*_
import pickle

# 演示序列化和反序列化

class Person():
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age

    def __str__(self) -> str:
        return '' + self.name+self.age+self.sex


if __name__ == '__main__':
    p = Person('Bevis','boy',23)

    # 存储到变量中
    dic = {'name':'bevis','age':23,'sex':'boy'}
    data = pickle.dumps(dic)

    print(pickle.loads(data).keys()) # dict_keys(['name', 'age', 'sex'])

    # 存储到文件中
    with open('pickle.pkl','wb') as pk:
        pickle.dump(dic,pk)

    with open('pickle.pkl','rb') as pk_:
        dic_ = pickle.load(pk_)
        print(dic_)             # {'name': 'bevis', 'age': 23, 'sex': 'boy'}

