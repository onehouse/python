'''
模仿静态变量(static)另一案例。演示一个python作用域使用方法。
'''

num = 1


class Stafunc(object):
    num = 1

    def add_static(self):
        print("内部的num是%d" % self.num)
        self.num += 1


static_num = Stafunc()
for i in range(3):
    print("外部的num是%d" % num, end =",")
    static_num.add_static()
    print("\n")
    num += 1