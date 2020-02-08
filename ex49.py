'''
使用lambda来创建匿名函数。
（格式：lambda[形参1，形参2，...] ：表达式）
'''

add = lambda x, y: x+y
minus = lambda x, y: x-y
m = int(input("输入m ="))
n = int(input("输入n ="))
print("m + n = ", add(m, n))
print("m - n = ", minus(m, n))