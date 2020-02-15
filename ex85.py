'''
输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
'''

x = int(input("输入一个奇数："))
i = 1
while 1:
    s = 10**i -1
    if s % x == 0:
        break
    i += 1
print("最少%d个9能被%d整除。即：" % (i, x))
print("%d = %d*%d" % (s, x, s/x))