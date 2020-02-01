'''
打印出所有的"水仙花数"，所谓"水仙花数"
是指一个三位数，其各位数字立方和等于该
数本身。例如：153是一个"水仙花数"，因
为153=1的三次方＋5的三次方＋3的三次方。（两种方法并比较效率。）
'''
import time
a = time.time()


def f1():
    for i in range(1, 10):
        for j in range(10):
            for k in range(10):
                if i * 100 + j * 10 + k == i ** 3 + j ** 3 + k ** 3:
                    print(i*100+j*10+k)


def f2():
    for i in range(100, 1000):
        j = i // 100
        k = i // 10 % 10
        l = i % 10
        if i == j ** 3 + k ** 3 + l ** 3:
            print(i)


f1()
b = time.time()
f2()
c = time.time()
print("方法一使用时间为：%s\n方法二使用时间为：%s" % (b-a, c-b))



