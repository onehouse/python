'''
利用递归方法求5!。
'''


def reduced_multiply(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*reduced_multiply(n-1)


# 此处求了从0到10的阶乘
for i in range(10):
    print("%d! = %d" % (i, reduced_multiply(i)))