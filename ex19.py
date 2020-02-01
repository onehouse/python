'''
一个数如果恰好等于它的因子之和，这个数就称为"完数"。
例如6=1＋2＋3.编程找出1000以内的所有完数。
'''


# 求因子的函数
def f(n):
    l = [1]
    for i in range(2, n):
        if n % i == 0:
            l.append(i)
    return l


# 按一定的格式输出完数
for i in range(2, 1001):
    if i == sum(f(i)):
        print("%d = " % i, end="")
        for j in f(i):
            if j != f(i)[-1]:
                print("%d + " % j, end="")
            else:
                print(j)