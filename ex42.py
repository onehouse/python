'''
学习使用auto定义变量的用法。
(即普通的局部变量)
'''

num = 2


def autofunc():
    num = 0
    print("内部的num是%d" % num)
    num += 1


for i in range(3):
    print("外部的num是%d" % num, end =",")
    autofunc()
    print("\n")
    num += 1